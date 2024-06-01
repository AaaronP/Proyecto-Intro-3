def create_trie_aux(trie, biblioteca):
    if not trie: return [0, [],[]]

    for prefix, freq in biblioteca.items():
        insert_prefix(trie, prefix, freq)

    return trie

def insert_prefix(trie, prefix, freq):
    v, left, right = trie
    pass


def create_trie(biblioteca):
    return create_trie_aux([], biblioteca)