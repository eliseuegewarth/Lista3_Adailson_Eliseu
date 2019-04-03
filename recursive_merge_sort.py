

def recursive_merge_sort(vector):
    vector_size = len(vector)
    if vector_size == 1:
        pass
    else:
        half_size = vector_size//2
        left = recursive_merge_sort(vector[:half_size])
        right = recursive_merge_sort(vector[half_size:])
        vector = copy_merge(left, right)
    return vector

def copy_merge(left, right):
    vector = []
    while(len(left) or len(right)):
        if len(left) and len(right):
            if right[0] > left[0]:
                vector.append(left[0])
                left.remove(left[0])
            else:
                vector.append(right[0])
                right.remove(right[0])
        elif len(left):
            for x in left:
                vector.append(x)
                left.remove(x)
        else:
            for x in right:
                vector.append(x)
                right.remove(x)
    return vector
