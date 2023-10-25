"""
Author - Sami Al-Jamal
Editor/Partner - Jack 
"""


def encoder(password):
    new_pass = ""
    for char in password:
        new_pass += str((int(char) + 3) % 10)
    return new_pass


def main():
    encode_pass = ""
    decode_pass = ""
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encode_pass = encoder(password)
            print(encode_pass)
            print("Your password has been encoded and stored!")
        elif option == 2:
            """
            Add decode function here
            """
        elif option == 3:
            break


if __name__ == "__main__":
    main()
