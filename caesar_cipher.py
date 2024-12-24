def caesar_cipher_encrypt(text, shift):
    shift = shift % 26  # Handle shifts greater than 26
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result += encrypted_char
        else:
            result += char  # Non-alphabet characters remain unchanged

    return result
