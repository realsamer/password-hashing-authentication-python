import hashlib
import os
import secrets


def register():
    username = input("Enter username: ").strip()

    if not username or ":" in username:
        print("Invalid username.")
        return

    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            for line in file:
                if line.split(":")[0] == username:
                    print("Username already exists.")
                    return

    password = input("Enter password: ")
    if not password:
        print("Password cannot be empty.")
        return

    salt = secrets.token_hex(16)
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

    with open("users.txt", "a") as file:
        file.write(username + ":" + salt + ":" + hashed_password + "\n")

    print("Registration successful!")


def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if not os.path.exists("users.txt"):
        print("Login failed.")
        return

    with open("users.txt", "r") as file:
        for line in file:
            data = line.strip().split(":")
            if len(data) == 3 and data[0] == username:
                salt = data[1]
                saved_hash = data[2]
                hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

                if hashed_password == saved_hash:
                    print("Login successful!")
                else:
                    print("Login failed.")
                return

    print("Login failed.")


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
