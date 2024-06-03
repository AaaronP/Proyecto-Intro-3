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

    return sorted(biblioteca.items(), key=lambda item: item[1], reverse=True)

# Crea el trie con listas
# Dominio: lista con tuplas de los prefijos y frecuencias
# Codominio: Un arbol binario trie [int, [list], [list]]
def create_trie(res):
    biblioteca = []
    for i in range(len(res)):
        x, y = res[i]
        biblioteca.append(([x, [], []], y))

    # Ordenando por la frecuencia
    biblioteca.sort(key=lambda x: x[1])

    while len(biblioteca) > 1:
        (prefix1, freq1) = biblioteca.pop(0)
        (prefix2, freq2) = biblioteca.pop(0)

        # fix
        node = [freq1 + freq2, prefix1, prefix2]
        
        biblioteca.append((node, freq1 + freq2))
        #print(biblioteca)
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
