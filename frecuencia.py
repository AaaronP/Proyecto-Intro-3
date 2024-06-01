def frecuancia(text):
    biblioteca = dict()

    for i in text:
        if i not in biblioteca:
            biblioteca[str(i)] = 1
        else:
            biblioteca[str(i)] += 1

    return sorted(biblioteca.items(), key=lambda item: item[1], reverse=True)

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print(frecuancia(text))
#{' ': 90, 'e': 59, 't': 43, 's': 39, 'n': 38, 'i': 32, 'a': 28, 'o': 25, 'r': 24, 'm': 18, 'p': 18, 'u': 17, 'l': 17, 'd': 16, 'h': 14, 'y': 13, 'g': 11, 'c': 10, 'k': 7, 'I': 6, 'f': 6, 'w': 6, 'L': 5, 'b': 5, 'v': 5, '.': 4, ',': 4, '0': 3, 'x': 2, '1': 2, "'": 1, '5': 1, '9': 1, '6': 1, 'A': 1, 'P': 1, 'M': 1}