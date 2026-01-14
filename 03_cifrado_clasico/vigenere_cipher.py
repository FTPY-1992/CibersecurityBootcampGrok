def vigenere_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypt plaintext using Vigenere cipher with given key.
    Only letters are encrypted; others caracters remain unchanged.
    :param plaintext: string to be encrypted
    :param key: integer key for encryption
    :return: encrypted string
    """

    result = []
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            #Determinate shift from key
            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            else:
                shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')

            result.append(chr(shifted))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypt by shifting backwards using the same key
    :param ciphertext:
    :param key:
    :return:
    """
    result = []
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                shifted = (ord(char) - ord('A') - shift) % 26 + ord('A')
            else:
                shifted = (ord(char) - ord('a') - shift) % 26 + ord('a')

            result.append(chr(shifted))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)