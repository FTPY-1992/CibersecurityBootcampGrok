
def caesar_encrypt(plaintext:str, shift:int) -> str:
    """
    Encrypt plaintext using Caesar cipher with given shift.
    Only letter are shifted, other remain unchanged.
    :param plaintext: str
    :param shift: int
    :return: str
    """
    result = []
    shift = shift % 26 # Normalize shift to 0-25
    for char in plaintext:
        if char.isupper():
            # A=65, Z=90
            shifted = (ord(char) - 65 + shift) % 26 + 65
            result.append(chr(shifted))
        elif char.islower():
            # a=97, z=122
            shifted = (ord(char) - 97 + shift) % 26 + 97
            result.append(chr(shifted))
        else:
            result.append(char) # No shift non-letters
    return ''.join(result)

def caesar_decrypt(ciphertext:str, shift:int) -> str:
    """
    Decrypt by shifting backwards.
    :param ciphertext: str
    :param shift: int
    :return: str
    """
    return caesar_encrypt(ciphertext, -shift)

def brute_force_caesar(ciphertext: str) -> list:
    """
    Try all 25 possible shifts and return possible plaintext.
    :param ciphertext: str
    :return: list
    """
    results = []
    for shift in range(1,26):
        plaintext = caesar_decrypt(ciphertext, shift)
        results.append(f"Shift {shift:2d}: {plaintext}")
    return results

def letters_frequency(text: str)-> dict:
    """
    Calculate frequency of letters in text (case-insensitive).
    Return a dict with letter: count percentage
    :param text: str
    :return: dict
    """
    freq={}
    total_letters=0

    for char in text.upper():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
            total_letters += 1

    if total_letters == 0:
        return {}

    for letter in freq:
        freq[letter] = (freq[letter] / total_letters) * 100

    return dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

def auto_decrypt_caesar(ciphertext: str)-> tuple[str,int]:
    """
    Attempt to auto-decrypt Caesar cipher by asumming most common letter is "E".
    Returns the most likely plaintext and shift
    :param ciphertext: str
    :return: tuple[str,int]
    """
    freq = letters_frequency(ciphertext)
    if not freq:
        return "Letters no found", 0
    # Most common letter in ciphertext
    most_common = next(iter(freq))

    #Most common in Spanish/English: 'E' (ACSII 69)
    e_ord = ord('E')
    most_common_ord= ord(most_common)

    #Calculate shift to make most_common become 'E'
    shift = (most_common_ord - e_ord) % 26
    plaintext = caesar_decrypt(ciphertext, shift)
    return plaintext, shift

def main_caesar():
    print("=== Caesar Cipher . Module 03 ===\n")

    action = input("Encrypt (e), Decrypt (d), or Brute Force (b)?")
    text = input("Enter text: ").strip()

    if action == "e":
        shift = int(input("Enter shift (1-25): "))
        encrypted = caesar_encrypt(text, shift)
        print(f"\nEncrypted: {encrypted}")
    elif action == "d":
        shift = int(input("Enter shift (1-25): "))
        decrypted = caesar_decrypt(text, shift)
        print(f"\nDecrypted: {decrypted}")
    elif action == "b":
        print("\nBrute Force Results:")
        results= brute_force_caesar(text)
        for res in results:
            print(res)
    else:
        print("Invalid Option")

if __name__ == "__main__":
    main_caesar()