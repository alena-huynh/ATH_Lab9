# Alena Huynh

# the encoder function
def encoder(password1):
    # makes sure the string passed in is in the form str

    password = str(password1)
    # validates the string length and makes sure password is only made of numeric characters

    if len(password) != 8 or not password.isdigit():
        return "Invalid password. Please enter an 8-digit password containing only numbers."

    # Encode each digit into an empty list
    encoded_digits = []
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded_digits.append(str(new_digit))

    # joins together the digits list into one string

    encoded_password = ''.join(encoded_digits)

    return encoded_password

def decode(newstring):
    newlist = []
    decodedstring = ""
    for i in range(len(newstring)):
        newlist.append(int(newstring[i]))
    final_list = [sublist - 3 for sublist in newlist]
    for i in range(len(final_list)):
        decodedstring = decodedstring + str(final_list[i])
    return decodedstring


# prints a menu

def main():
    # loops until the user chooses to quit
    while True:
        choice = 0
        while choice != 3:
            print("Menu")
            print("-------------")
            choice = int(input("1. Encode\n2. Decode\n3. Quit\n"))

            # function calls depending on user input
            if choice == 1:
                encoded_password = encoder(input("Please enter your password to encode: "))
            elif choice == 2:
                decodedstring = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decodedstring}\n")
                pass
            elif choice == 3:
                quit()


if __name__ == "__main__":
    main()