def aggregate_frequency(text):
    freq: dict = dict()
    for c in text:
        freq[c] = freq.get(c, 0) + 1

    return sorted(freq.items(), key=lambda item: item[1], reverse=True)


freq_list = aggregate_frequency("BDDAAAABACEBBBAA")
print(freq_list)
