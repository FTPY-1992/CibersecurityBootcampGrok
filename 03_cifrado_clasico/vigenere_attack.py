def find_repeated_sequences(text: str, min_length: int = 3) -> dict:
    """
    Kasiski test: find repeated sequences and their distances.
    Returns dict of sequence -> list of distances between repetitions.
    :param text:
    :param min_length:
    :return:
    """
    text = text.upper()
    sequences = {}

    for length in range(min_length, min_length + 10):
        for i in range(len(text) - length):
            seq = text[i:i + length]
            if seq.isalpha():
                positions = [j for j in range(i, len(text) - length + 1) if text[j:j+length] == seq]
                if len(positions) > 1:
                    distances = [positions[k+1] - positions[k] for k in range(len(positions) - 1)]
                    if seq in sequences:
                        sequences[seq].extend(distances)
                    else:
                        sequences[seq] = distances

    return sequences