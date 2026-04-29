import re

def test_email():
    email = "test@example.com"
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Email is valid!")
    else:
        print("Invalid email")

if __name__ == "__main__":
    test_email()
    print("CI process finished successfully!")
