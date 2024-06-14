import sys
import re
import bitarray as bit


def get_table(path_table):
    diccionario = {}
    with open(path_table, "r") as ar:
        for i in ar:
            txt = i.strip().split()

            # validar si el prefix es ' '
            if len(txt) == 2:
                prefix = txt[0]
                freq = txt[1]

                diccionario[prefix] = freq
            else:
                diccionario[" "] = txt[0]
    return diccionario


def get_stats(path_stats):
    freq = []
    txt = ""
    with open(path_stats, "r") as p:
        txt = p.read()

    freq_list = re.search(r"Tabla de frecuencias: (\[.*\])", txt).group(1)

    freq = eval(freq_list)

    return freq


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


def translate(trie, binary):
    original = trie
    txt = ""
    i = 0
    current_trie = trie

    while i < len(binary):
        v, left, right = current_trie

        # verificamos que el nodo destino sea de tipo string
        if not left and not right and isinstance(v, str):
            txt += v
            current_trie = original
        else:
            bit = int(binary[i])
            if bit == 0 and left:
                current_trie = left
                i += 1
            elif bit == 1 and right:
                current_trie = right
                i += 1
            else:
                current_trie = original

        if current_trie == original and i < len(binary) and str(binary[i]) not in "01":
            i += 1

    return txt


def main():
    bits = bit.bitarray()

    path_table = ""
    path_huff = ""
    path_stats = ""

    if len(sys.argv) <= 1:
        print("hola, no tiene argumentos")
    else:
        path_huff = sys.argv[1]
        path_table = sys.argv[2]
        path_stats = sys.argv[3]

    with open(path_huff, "rb") as bt:
        bits.fromfile(bt)

    table = get_table(path_table)
    stats = get_stats(path_stats)

    trie = create_trie(stats)
    text = translate(trie, bits)

    with open(path_huff[:-5], "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
