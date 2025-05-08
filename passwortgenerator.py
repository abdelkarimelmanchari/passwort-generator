import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%^&*()"

def generate_password(length, count, use_special_chars=True):
    if not use_special_chars:
        chars_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    else:
        chars_set = chars

    for _ in range(count):
        password = ''.join(random.choice(chars_set) for _ in range(length))
        print("Here is your password:", password)

def main():
    print("Note: Passwords shorter than 8 characters are not recommended for security reasons.")

    while True:
        try:
            length = int(input("What length would you like your password to be: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if length < 8:
            print("The requested length is lower than 8. Do you wish to continue anyway? (yes/no)")
            if input().strip().lower() != "yes":
                continue

        try:
            count = int(input("How many passwords would you like: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        print("Would you like special characters? (yes/no)")
        special = input().strip().lower() == "yes"

        generate_password(length, count, use_special_chars=special)

        print("Do you want to generate more passwords? (yes/no)")
        if input().strip().lower() != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
