from collections import Counter


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