'''
Module providing a function that encodes or decodes a
message provided with the ceasar cipher method.

# Gioele Amendola
# 29/04/2024

# Create functions for encrypting and decrypting a message using the Caesar cipher.
# Allow the user to specify the shift value (number of positions to shift each letter).
# Handle both encryption and decryption using the same function with appropriate adjustments.
# Encrypt and decrypt the given message using the specified shift value.
'''
import string


def en_dec(message: str, shift: int = None):
    '''
    Main function to call. Given a message and a shift, call
    the encryption or decryption function and returns the returned message.

    Args:
        message (str): a string of text.
        shift (int, optional): the amount of shifts wanted to encrypt or decrypt the message.
        Defaults to None.

    Raises:
        ValueError: raised when the message is not an ASCII character.
        ValueError: raised if inputted shift is not an integer.
        ValueError: raised if inputted choose is not an integer.

    Returns:
        str: returns the encoded or decoded message.
    '''

    # Check if message is an ASCII char
    if not message.isascii():
        raise ValueError("message not valid.")

    print("\nWelcome to the Ceasar Chiper Encryption/Decryption\n")

    # Checks if shift has been passed as an argument
    if shift is None:
        while True:
            try:
                shift = int(
                    input("input number of shift (press Enter for None)> "))
            except ValueError:
                print("Invalid Input.")
            else:
                break

    # Asks if the message needs to be encrypted or decrypted
    # They do the exact same thing but opposite of eachother
    while True:
        print(f"Message given:\n {message}\nPosition shift:\n {shift}\n")
        try:
            choose: int = int(input("1. Encrypt\n2. Decrypt\n> "))
        except ValueError:
            print("Invalid Input")
        else:
            break

    if choose == 1:
        return encrypt(message, shift)
    if choose == 2:
        return decrypt(message, shift)
    return None


def encrypt(message: str, shift: int) -> str:
    '''
    Encrypts a message following the ceasar cipher method with given shift.

    Args:
        message (str): text that needs to be encrypted.
        shift (int): the amount of shifts wanted for the encryption.

    Returns:
        str: encrypted message.
    '''
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


def decrypt(message: str, shift: int) -> str:
    '''
    Decrypts a message following the ceasar cipher method with given shift.

    Args:
        message (str): text that needs to be decrypted.
        shift (int): the amount of shifts needed fot the decryption.

    Returns:
        str: decrypted message.
    '''
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
text1: str = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
              " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
print(en_dec(text1, 10))
text2: str = ("Vycow szdfw nyvyc dse kwoe, myxdomeoefc knszsdmsxq ovse," +
              " don ny osfdwyn eowzyc sxmsnsnfxe fe vklyco oe nyvyco wkqxk kvsbfk.")
print(en_dec(text2, 10))
