def encoder(password1):
    password = str(password1)
    if len(password) != 8 or not password.isdigit():
        return "Invalid password. Please enter an 8-digit password containing only numbers."

    # Encode each digit
    encoded_digits = []
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded_digits.append(str(new_digit))

    encoded_password = ''.join(encoded_digits)
    print("Your password has been encoded and stored!")

    return encoded_password


def main():
    print("Menu")
    print("-------------")
    choice = int(input("1. Encode\n2. Decode\n3. Quit\n"))


    if choice == 1:
        encoder(input("Please enter your password to encode: "))
    elif choice == 2:
        pass
    elif choice == 3:
        quit()


if __name__ == "__main__":
    main()