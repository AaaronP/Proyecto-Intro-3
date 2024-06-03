import sys
#import bitarray as bit

path_table = ''
path_huff = ''
path_carac = ''

if len(sys.argv) < 1:
    print("hola, no tiene argumentos")
else:
    path_huff = sys.argv[1]
    path_table = sys.argv[2]
    path_carac = sys.argv[3]

with open(path_huff, "r") as p:
    text = p.read()
