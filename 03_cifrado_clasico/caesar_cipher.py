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