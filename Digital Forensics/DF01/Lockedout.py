import hashlib
import random
import base64

# Simple login validation program
def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Users database simulation
users = {
    'admin': hash_pass('superSecure123'),
    'guest': hash_pass('guest')
}

def authenticate(username, password):
    hashed = hash_pass(password)
    if username in users:
        if hashed == users[username]:
            return True
    return False

# Main loop
def main():
    print("=== Welcome to SecureApp ===")
    attempts = 0

    while attempts < 5:
        username = input("Username: ")
        password = input("Password: ")

        if authenticate(username, password):
            if username == 'admin':
                print("Access Granted! Welcome, admin!")
                return
            else:
                print(f"Welcome {username}! You have limited privileges.")
                return
        else:
            attempts += 1
            print(f"Invalid credentials! Attempts left: {5 - attempts}")

    lockout_msg = "Account locked. Contact admin."
    randomized_msg = ''.join(random.sample(lockout_msg, len(lockout_msg)))

    if randomized_msg == lockout_msg:
        encoded_flag = "TEtTU01LSkFLVVR7VW5sMGNrX1I0bmQwbV9MMGNrMHV0fQ=="
        print(base64.b64decode(encoded_flag).decode())
    else:
        print(randomized_msg)

# The bug here is intentionally hidden and tricky to spot. Good luck!
if __name__ == "__main__":
    main()
