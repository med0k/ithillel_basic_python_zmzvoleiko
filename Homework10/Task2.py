import random
import string


def generate_password(length):
    valid_chars = string.ascii_letters + string.digits + '_'

    while True:
        password = ''.join(random.choice(valid_chars) for i in range(length))

        if (any(char.isupper() for char in password)
                and any(char.islower() for char in password)
                and any(char.isdigit() for char in password)
                and not any(password[i] == password[i + 1] == char for i, char in enumerate(password[:-2]))):
            break
    return password


def main():
    rsult = generate_password(8)
    print(f"Your generated password is {rsult}")


if __name__ == "__main__":
    main()
