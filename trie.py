def create_trie(biblioteca):

    while len(biblioteca) > 1:
        (prefix1, freq1) = biblioteca.pop(0)
        (prefix2, freq2) = biblioteca.pop(0)

        node = [freq1 + freq2, [prefix1, [], []], [prefix2, [], []]]

        biblioteca.append((node, freq1 + freq2))

        biblioteca.sort(key=lambda x: x[1])

    return biblioteca[0][0]

biblioteca = [('o', 2), ('H', 1), ('l', 1), ('a', 1), (' ', 1), ('m', 1), ('u', 1), ('n', 1), ('d', 1)]
print(create_trie(biblioteca))