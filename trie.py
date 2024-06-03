# Obtener los prefijos y su frecuencia
# Domino: string
# Codomino: lista de tuplas [(x: str, y: int), (...)]
def frecuancia(text):
    biblioteca = dict()

    for i in text:
        if i not in biblioteca:
            biblioteca[str(i)] = 1
        else:
            biblioteca[str(i)] += 1

    # ordena las tuplas por su frecuencia
    return sorted(biblioteca.items(), key=lambda item: item[1])

# Crea el trie con listas
# Dominio: lista con tuplas de los prefijos y frecuencias
# Codominio: Un arbol binario trie [int, [list], [list]]
def create_trie(prefixs):
    # transforma los prefijos en la forma [prefix, [], []]
    biblioteca = []
    for i in range(len(prefixs)):
        x, y = prefixs[i]
        biblioteca.append(([x, [], []], y))

    while len(biblioteca) > 1:
        (prefix1, freq1) = biblioteca.pop(0)
        (prefix2, freq2) = biblioteca.pop(0)

        node = [freq1 + freq2, prefix1, prefix2]
        
        biblioteca.append((node, freq1 + freq2))
        biblioteca.sort(key=lambda x: x[1])

    return biblioteca[0][0]

# Obtenie el codigo para cada prefijo
# Dominio: un arbol trie
# Codominio: una lista con tuplas [(prefix, '010'), (...)]
def translate(trie, camino=''):
    if not trie: return []

    v, left, right = trie

    if not left and not right: return [(v, camino)]

    L = translate(left, camino + '0')
    R = translate(right, camino + '1')

    return L + R    

biblioteca = frecuancia('Hola mundo')
trie = create_trie(biblioteca)
print(translate(trie))
