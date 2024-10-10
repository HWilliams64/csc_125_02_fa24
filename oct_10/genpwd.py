import hashlib

while True:
    password_str = input("Enter your password:")
    password_hash = hashlib.sha256(password_str.encode()).hexdigest()
    print(password_hash)
