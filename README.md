# Password Hashing Authentication (Python)

A simple Python program for the **Software Security - Chapter 3** assignment.
It allows users to register and log in using salted SHA-256 password hashes.

## Run

```bash
python password_auth.py
```

On Windows, you can also use `py password_auth.py`.
No extra libraries are needed.

## How it works

- **Register:** Enter a username and password. The program creates a random salt and saves the username, salt, and password hash in `users.txt`.
- **Login:** Enter your username and password. The program uses the saved salt to check if the password is correct.
- The actual password is **not saved** in the file.

`users.txt` is created automatically and is excluded from Git.

**Note:** This is a college demonstration. Real applications should use a password hashing algorithm designed for passwords, such as Argon2id.
