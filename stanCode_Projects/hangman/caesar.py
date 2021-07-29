"""
File: caesar.py
Name: David
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program decipher the Caesar Cipher.
    """
    while True:
        # Ensure the secret number inputted is an integer.
        secret_number = input("Secret number: ")
        if secret_number.isdigit():
            secret_number = int(secret_number)
            break
        print("Sorry. The secret number must be an integer!")
        # If the secret number is not an integer, ask users to enter again.
    new_set = new_alphabet(secret_number)
    # Create the alphabet with the new order decided by the secret number.
    ciphered_string = input("What's the ciphered string? ")
    ciphered_string = ciphered_string.upper()
    # Case-insensitive
    print("The deciphered string is: "+str(decipher(ciphered_string, new_set)))
    # Use decipher() function to decipher the string.


def new_alphabet(secret_number):
    """
    Create the alphabet with the new order.
    :param secret_number: the number of translation
    :return: the alphabet with the new order
    """
    new = ""
    for i in range(len(ALPHABET)-secret_number, len(ALPHABET)):
        # Concatenate the alphabets translated to the front of the alphabet string.
        new += ALPHABET[i]
    for j in range(len(ALPHABET)-secret_number):
        # Concatenate the remaining alphabets.
        new += ALPHABET[j]
    return new


def decipher(ciphered_string, new_set):
    """
    :param ciphered_string: the string to be deciphered
    :param new_set: the alphabets string with the new order.
    :return: deciphered string
    """
    ans = ""
    for i in range(len(ciphered_string)):
        if ciphered_string[i].isalpha():
            # Decipher the string only when the element is an alphabet.
            w = new_set.find(ciphered_string[i])
            # Find the new position of the alphabet.
            ans += ALPHABET[w]
            # Concatenate the original alphabet.
        else:
            # The elements that are not alphabets remain the same.
            ans += ciphered_string[i]
    return ans


#  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
