def get_merged_sequence(seq1, seq2):
    merged = []
    i = 0
    j = 0
    while i < len(seq1) and j < len(seq2):
        if seq1[i] == seq2[j]:
            if len(merged) == 0 or merged[-1] != seq1[i]:
                merged.append(seq1[i])
            i += 1
            j += 1
            print(i, j)
        elif seq1[i] < seq2[j]:
            i += 1
        else:
            j += 1
    return merged
