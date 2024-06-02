def frecuancia(text):
    biblioteca = dict()

    for i in text:
        if i not in biblioteca:
            biblioteca[str(i)] = 1
        else:
            biblioteca[str(i)] += 1

    return sorted(biblioteca.items(), key=lambda item: item[1], reverse=True)

text = "Hola mundo"

print(frecuancia(text))
#{' ': 90, 'e': 59, 't': 43, 's': 39, 'n': 38, 'i': 32, 'a': 28, 'o': 25, 'r': 24, 'm': 18, 'p': 18, 'u': 17, 'l': 17, 'd': 16, 'h': 14, 'y': 13, 'g': 11, 'c': 10, 'k': 7, 'I': 6, 'f': 6, 'w': 6, 'L': 5, 'b': 5, 'v': 5, '.': 4, ',': 4, '0': 3, 'x': 2, '1': 2, "'": 1, '5': 1, '9': 1, '6': 1, 'A': 1, 'P': 1, 'M': 1}
#[('o', 2), ('H', 1), ('l', 1), ('a', 1), (' ', 1), ('m', 1), ('u', 1), ('n', 1), ('d', 1)]