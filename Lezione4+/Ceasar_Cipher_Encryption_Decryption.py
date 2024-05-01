# Gioele Amendola
# 29/04/2024

# Create functions for encrypting and decrypting a message using the Caesar cipher.
# Allow the user to specify the shift value (number of positions to shift each letter).
# Handle both encryption and decryption using the same function with appropriate adjustments.
# Encrypt and decrypt the given message using the specified shift value.

import string

def en_dec(message:str,shift:int = None):

    # Check if message is an ASCII char
    if not message.isascii():
        raise ValueError("message not valid.")
    
    print("\nWelcome to the Ceasar Chiper Encryption/Decryption\n")

    # Checks if shift has been passed as an argument
    if shift is None:
        while True:
            try:
                shift = int(input("input number of shift (press Enter for None)> "))
            except:
                print("Invalid Input.")
            else:
                break
    
    # Asks if the message needs to be encrypted or decrypted
    # They do the exact same thing but opposite of eachother
    while True:
        print(f"Message given:\n {message}\nPosition shift:\n {shift}\n")
        try:
            choose: int = int(input("1. Encrypt\n2. Decrypt\n> "))
        except:
            print("Invalid Input")
        else:
            break

    endec_message: str = ""
    if choose == 1:
        endec_message = encrypt(message,shift)
    elif choose == 2:
        endec_message = decrypt(message,shift)

    return endec_message


def encrypt(message: str,shift: int) -> str:

    endec_message: str = ""
    uppercase: str = string.ascii_uppercase
    lowercase: str = string.ascii_lowercase

    for char in message:
        pos: int = -1
        if char.isalpha():
            pos = lowercase.index(char.lower()) + shift
            if pos > 25:
                pos -= 25
            endec_message += lowercase[pos] if char.islower() else uppercase[pos]
        else:
            endec_message += char

    return endec_message

def decrypt(message: str,shift: int) -> str:
    endec_message: str = ""
    uppercase: str = string.ascii_uppercase
    lowercase: str = string.ascii_lowercase

    for char in message:
        pos: int = -1
        if char.isalpha():
            pos = lowercase.index(char.lower()) - shift
            if pos < 0:
                pos += 25
            endec_message += lowercase[pos] if char.islower() else uppercase[pos]
        else:
            endec_message += char

    return endec_message

# Example Test:
text1: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print(en_dec(text1,10))
text2: str = "Vycow szdfw nyvyc dse kwoe, myxdomeoefc knszsdmsxq ovse, don ny osfdwyn eowzyc sxmsnsnfxe fe vklyco oe nyvyco wkqxk kvsbfk."
print(en_dec(text2,10))