def create_trie_aux(trie, biblioteca):
    res = []
    for i in range(len(biblioteca)-1):
        prefix, freq = biblioteca[i]
        prefix2, freq2 = biblioteca[i+1]
        if freq == freq2:
            res.append([freq + freq2, [prefix, [], []], [prefix2, [], []]])
    print(res)

def create_trie(biblioteca):
    return create_trie_aux([], biblioteca)

biblioteca = [(' ', 90), ('e', 59), ('t', 43), ('s', 39), ('n', 38), ('i', 32), ('a', 28), ('o', 25), ('r', 24), ('m', 18), ('p', 18), ('u', 17), ('l', 17), ('d', 16), ('h', 14), ('y', 13), ('g', 11), ('c', 10), ('k', 7), ('I', 6), ('f', 6), ('w', 6), ('L', 5), ('b', 5), ('v', 5), ('.', 4), (',', 4), ('0', 3), ('x', 2), ('1', 2), ("'", 1), ('5', 1), ('9', 1), ('6', 1), ('A', 1), ('P', 1), ('M', 1)]

print(create_trie(biblioteca[::-1]))