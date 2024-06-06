import sys
import bitarray as bit

bits = bit.bitarray()

path_table = ""
path_huff = ""
path_stats = ""

stats_text = ""
huff_text = ""

if len(sys.argv) < 1:
    print("hola, no tiene argumentos")
else:
    path_huff = sys.argv[1]
    path_table = sys.argv[2]
    path_stats = sys.argv[3]

with open(path_huff, "rb") as bt:
    bits.fromfile(bt)


with open(path_stats, "r") as p:
    stats_text = p.read()


def get_table():
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


print(get_table())
