import bitarray as bit
import sys
import os


# Obtener los prefijos y su frecuencia
# Domino: string
# Codomino: lista de tuplas [(x: str, y: int), (...)]
def frecuencia(text):
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
# Codominio: Un arbol binario trie [raiz, [], []]
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


# Obtiene el codigo para cada prefijo
# Dominio: un arbol trie
# Codominio: una lista con tuplas [(prefix, '010'), (...)]
def translate(trie, camino=""):
    if not trie:
        return []

    v, left, right = trie

    if not left and not right:
        return [(v, camino)]

    L = translate(left, camino + "0")
    R = translate(right, camino + "1")

    return L + R


# Obtiene la altura del arbol trie
# Dominio: Un arbol binario trie
# Codominio: Un numero natural
def altura_trie(trie):
    if not trie:
        return 0

    v, left, right = trie

    if not left and not right:
        return 0

    ml = -1
    mr = -1

    if left:
        ml = max(ml, altura_trie(left) + 1)
    if right:
        mr = max(mr, altura_trie(right) + 1)

    return max(ml, mr)


# Obtiene el ancho del trie
# Dominio: Un arbol binario trie
# Codominio: Un numero natural
def ancho_trie(trie):
    if not trie:
        return 0

    S = [(trie, 0)]
    cLevel = 0
    maxAux = 0
    maxAncho = 0

    while S:
        nodo, level = S.pop(0)

        if level == cLevel:
            maxAux += 1
        else:
            maxAncho = max(maxAncho, maxAux)
            cLevel = level
            maxAux = 1

        if nodo[1]:
            S.append((nodo[1], level + 1))
        if nodo[2]:
            S.append((nodo[2], level + 1))

    maxAncho = max(maxAncho, maxAux)
    return maxAncho


# Devuelve la cantidad de nodos por nivel
# Dominio: Un arbol binario trie
# Codominio: Una lista con numeros naturales
def nodos_nivel(trie):
    if not trie:
        return []

    S = [(trie, 0)]
    cLevels = []

    while S:
        nodo, level = S.pop(0)

        if len(cLevels) <= level:
            cLevels.append(0)

        cLevels[level] += 1

        if nodo[1]:
            S.append((nodo[1], level + 1))
        if nodo[2]:
            S.append((nodo[2], level + 1))

    return cLevels


# Crea el archivo huff
# Dominio: Una lista con tuplas donde la x es el prefijo y el y es el codigo binario
# Codominio: Nada (None), crea el archivo .huff
def create_huff(codigos, text, path_file):
    binary = ""
    diccionario = {}

    for i in codigos:
        diccionario[i[0]] = i[1]

    for i in text:
        binary += diccionario[i]

    bits = bit.bitarray(binary)

    with open(f"{path_file}.huff", "wb") as bf:
        bits.tofile(bf)

    return bits


# Crea el archivo stats
# Dominio: Un arbol binario trie y la tabla de frecuencias
# Codominio: Nada (None). Crea el archivo .stats
# [(prefijo, frecuencia: int)]
def create_stats(trie, tablaFreq, path_file, bits):
    altura = altura_trie(trie)
    ancho = ancho_trie(trie)
    nodosNivel = nodos_nivel(trie)

    stats = {
        "Altura del arbol": altura,
        "Anchura del arbol": ancho,
        "Cantidad de nodos por nivel": nodosNivel,
        "Tabla de frecuencias": tablaFreq,
        "Longitud": len(bits),
    }

    with open(f"{path_file}.stats", "w") as file:
        for key, value in stats.items():
            file.write(f"{key}: {value}\n")


# Dominio: Una lista con tuplas donde la x es el prefijo y el y es el codigo binario
# Codominio: Nada (None). Crea el archivo .table
def create_table(codigos, path_file):
    # [prefijo, codigo]
    tabla = []

    # cambia los parentesis redondos por cuadrados
    for i, y in codigos:
        tabla.append([i, y])

    # Ordenada de menor a mayor a razon de su cantidad de bits
    tableSorted = sorted(tabla, key=lambda x: len(list(x[1])))

    lineas = []
    for fila in tableSorted:
        linea = rf"{fila[0].encode('unicode_escape').decode()}  {fila[1]}"
        lineas.append(linea)

    contenido = "\n".join(lineas)

    name_file = f"{path_file}.table"
    with open(name_file, "w") as f:
        f.write(contenido)


def main():
    path_file = ""
    text = ""

    if len(sys.argv) <= 1:
        print("El programa no tiene argumentos")
        return -1

    path_file = sys.argv[1]
    with open(path_file, "r") as h:
        text = h.read()

    # [(prefix, freq), (...)]
    biblioteca = frecuencia(text)
    trie = create_trie(biblioteca)
    codigos = translate(trie)

    bits = create_huff(codigos, text, path_file)
    create_table(codigos, path_file)
    create_stats(trie, biblioteca, path_file, bits)

    print(f"{path_file}.huff {path_file}.table {path_file}.stats")

    # Files bits size
    print(path_file, os.stat(path_file).st_size, "bits")
    print(f"{path_file}.huff", os.stat(f"{path_file}.huff").st_size, "bits")


if __name__ == "__main__":
    main()
