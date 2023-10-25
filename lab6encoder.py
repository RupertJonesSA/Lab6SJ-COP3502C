"""
Author - Sami Al-Jamal
Editor/Partner - Jack McKee
"""


def encoder(password):
    new_pass = ""
    for char in password:
        new_pass += str((int(char) + 3) % 10)
    return new_pass


def decode(encoded_password):
    decoded_password = ""
    for i in encoded_password:
        if int(i) in range(3, 10):
            decoded_password += str(int(i) - 3)
        elif int(i) == 0:
            decoded_password += "7"
        elif int(i) == 1:
            decoded_password += "8"
        elif int(i) == 2:
            decoded_password += "9"

    return decoded_password


def main():
    encode_pass = ""
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encode_pass = encoder(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            decoded_password = decode(encode_pass)
            print(f"The encoded password is {encode_pass}, and the original password is {decoded_password}.\n")

        elif option == 3:
            break


if __name__ == "__main__":
    main()
