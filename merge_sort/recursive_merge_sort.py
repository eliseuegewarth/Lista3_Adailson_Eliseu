
def recursive_merge_sort(vector, key=lambda x:x):
    # Algoritmo de merge recursivo
    vector_size = len(vector)
    if vector_size == 1:
        pass
    else:
        half_size = vector_size//2
        left = recursive_merge_sort(vector[:half_size], key)
        right = recursive_merge_sort(vector[half_size:], key)
        vector = copy_merge(left, right, key)
    return vector

def copy_merge(left, right, key = lambda x:x):
    # gera novo vetor mesclando o elementos das suas listas
    vector = []
    i = 0
    j = 0
    while(i < len(left) or j < len(right)):
        if i < len(left) and j < len(right):
            if key(right[j]) > key(left[i]):
                vector.append(left[i])
                i = i + 1
            else:
                vector.append(right[j])
                j = j + 1
        elif i < len(left):
            for x in range(i, len(left)):
                vector.append(left[i])
                i = i + 1
        else:
            for x in range(j, len(right)):
                vector.append(right[j])
                j = j + 1
    return vector
