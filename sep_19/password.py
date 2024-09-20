import hashlib

user_name = input("Enter a username: ")
password = input("Enter a password: ")

hashed_password = hashlib.sha256((user_name+password).encode()).hexdigest()
print("Hashed password:", hashed_password)
