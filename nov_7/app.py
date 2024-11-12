import shutil, json, os, hashlib, sys
import typing
from csc_125_02_fa24.nov_5.notetaker import input_number
# Functions:
# [x] Save DB
# [x] Load DB
# [x] Create account
# [x] Create password
# [x] Create username
# - Login
# - Save note
# - Load note
# - (optional) Reset password
# - (optional) OTP

def save_db(db_name:str, data:dict) -> None:
    backup_file = f"{db_name}.bak"
    if os.path.exists(db_name):
        # backup the DB before saving
        shutil.copy2(db_name, backup_file)

    # Overwrite the DB with the new data
    with open(db_name, 'w') as f:
        json.dump(data, f)

    if os.path.exists(backup_file):
        # remove the backup
        os.remove(backup_file)

def load_db(db_name:str) -> dict:
    if not os.path.exists(db_name):
        return {}

    with open(db_name, 'r') as f:
        return json.load(f)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def validate_username(db_name: str,  username: str) -> str:
    if 3 > len(username) > 20:
        return "Username must be between 3 and 20 characters long."

    db = load_db(db_name)

    users = db.setdefault("users", [])

    for user in users:
        if user["username"] == username:
            return f"The username '{username}' already exists."

    return ""


def create_account(db_name:str, username: str, password: str) -> str:
    db = load_db(db_name)

    error_message = validate_username(db_name, username)
    if error_message:
        return error_message

    new_user = {
        "username": username, 
        "password_hash": hash_password(password),
        "login_attempts": 0
    }

    users = db.setdefault("users", [])
    users.append(new_user)

    save_db(db_name, db)

    return "Account created successfully!!!"


def login(db_name: str, username: str, password: str) -> typing.Optional[dict]:
    db = load_db(db_name)

    users = db.setdefault("users", [])

    for user in users:
        if user["username"] == username:
            # Check that the user is not locked out
            if user["login_attempts"] > 4:
                return None
            else:
                # Add an attempt to the login attempts
                user["login_attempts"] += 1 
                save_db(db_name, db)

            # If the password is correct
            # - reset the login attempts
            # - return the user
            if user["password_hash"] == hash_password(password):
                user["login_attempts"] = 0
                save_db(db_name, db)
                return user
                
        
    return None


if __name__ == "__main__":
    DB_NAME = "app-db.json"

    while True:
        option:int = input_number("\nChoose an option:\n1. Create account\n2. Login\n3. Exit\n")

        # Create Account
        if option == 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            msg = create_account(DB_NAME, username, password)
            print(msg)

        # Login
        elif option == 2:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            user = login(DB_NAME, username, password)

            if not user:
                print("Invalid username or password.")
            else:
                print("Login successful.")

        elif option == 3:
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")
        print("="*80)
