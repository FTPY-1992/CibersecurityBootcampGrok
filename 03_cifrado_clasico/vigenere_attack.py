from collections import Counter
from vigenere_cipher import vigenere_decrypt


def extract_sequences(text:str, length: int) -> list:
    """
    Extract all alphabetic sequences of given length from text.
    :param text:
    :param length:
    :return: List of (sequence, starting positions)
    """

    text = text.upper()
    seq_positions = {}

    for i in range(len(text) - length + 1):
        seq = text[i:i + length]
        if seq.isalpha():
            if seq in seq_positions:
                seq_positions[seq].append(i)
            else:
                seq_positions[seq] = [i]

    return [(seq,pos) for seq,pos in seq_positions.items() if len(pos) > 1]

def calculate_distances(positions: list) -> list:
    """
    Calculate distances between consecutive repetitions in positions.
    :param positions:
    :return:
    """
    return [positions[k+1] - positions[k] for k in range(len(positions) - 1)]

def find_repeated_sequences(text: str, min_length: int = 3) -> dict:
    """
    Kasiski test: find repeated sequences and their distances.
    Returns dict of sequence -> list of distances between repetitions.
    :param text:
    :param min_length:
    :return:
    """
    sequences = {}

    for length in range(min_length, min_length + 10):
        seq_pos_list = extract_sequences(text, length)

        for seq, positions in seq_pos_list:
            distances = calculate_distances(positions)
            if seq in sequences:
                sequences[seq].append(distances)
            else:
                sequences[seq] = distances

    return sequences

def estimate_key_length(text: str) -> int:
    """
    Estimate key length using Kasiski distances (most common factor)
    :param text:
    :return:
    """
    sequences = find_repeated_sequences(text)

    if not sequences:
        return 1 #Fallback

    all_distances = []

    for distances in sequences.values():
        all_distances.extend(distances)

    if not all_distances:
        return 1

    #Contamos factores comunes (simplificado)
    factor_count = Counter()
    for d in all_distances:
        for factor in range(2, d+1):
            if d % factor == 0:
                factor_count[factor] += 1

    if not factor_count:
        return 1

    #la longitud mas probable es el factor con mas apariciones
    likely_length = factor_count.most_common(1)[0][0]
    return likely_length

def frequency_analysis_substrings(text: str, key_length: int) -> list:
    """
    Split text into key_length substrings and analyze frequency for each.
    Returns list of most likely shift for each position.
    :param text:
    :param key_length:
    :return:
    """

    text = text.upper()
    shifts = []

    for pos in range(key_length):
        substring = text[pos::key_length] #cada subalfabeto
        if not substring:
            shifts.append(0)
            continue

        freq = Counter(c for c in substring if c.isalpha())
        if not freq:
            shifts.append(0)
            continue

        most_common = freq.most_common(1)[0][0]
        #Asumimos que la mas comun es 'E' (ASCII 69)
        shift = (ord(most_common) - ord('E')) % 26
        shifts.append(shift)

    return shifts

def crack_vigenere(ciphertext: str) -> tuple[str,str]:
    """
    Attempt to crack Vigenere ciphertext using Kasiski and frequency analysis.
    Returns (estimated key, decrypted text)
    :param ciphertext:
    :return:
    """

    key_length = estimate_key_length(ciphertext)
    print(f"Estimated key length: {key_length}")

    shifts = frequency_analysis_substrings(ciphertext, key_length)

    #Convert shifts to letters (A=0 -> 'A', etc)
    key = ''.join(chr(ord('A') + s) for s in shifts)
    decrypted_text = vigenere_decrypt(ciphertext, key)

    return key, decrypted_text