import hashlib
import sys
# This is a our authentication application
# A user will have a user name and a password
# The password will be hashed using hashlib.sha256
# The user's information will be saved in a list of dictionaries 



db = {
    "users":[
        {
            "username": "admin",
            "password": "8e70fdbd0400b7a21539fd15fb4ab86c129f7cbd99261dbb0d95c18df8dec177"
        },
        {
            "username": "user1",
            "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
        },
        {
            "username": "user2",
            "password": "f5903f51e341a783e69ffc2d9b335048716f5f040a782a2764cd4e728b0f74d9"
        }
    ]
}

def password_check(inputted_password:str, password_hash:str) -> bool:
    inputted_password_bytes = inputted_password.encode()
    inputted_password_hash = hashlib.sha256(inputted_password_bytes).hexdigest()
    does_match = inputted_password_hash == password_hash
    return does_match


def get_user(username: str, users: list) -> dict:
    for user in users:
        if username == user['username']:
            return user

    return {}

if __name__ == '__main__':  
    while True:
        ui = input("Enter 'login' or 'exit': ")
        if ui == 'exit':
            sys.exit(0)
        elif ui == 'login':
            username = input("Enter username: ")
            password = input("Enter password: ")

            user = get_user(username, db['users'])

            is_password_correct = password_check(password, user.get('password', ''))

            if is_password_correct:
                print("Welcome to our application!")
            else:
                print("Username or password is incorrect. Please try again.")
        else:
            print("Invalid command. Please try again.")

    