import time
import sys
from gera_vector import gera_vector

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

def main(number_of_elements=10000, start_of_range=0, end_of_range=100000):
    vector = gera_vector([start_of_range, end_of_range], number_of_elements)
    start = time.time()
    vector = recursive_merge_sort(vector)
    end = time.time()
    time_in_ms = (int(1000*1000*(end-start)))/1000
    print("Ordenou {} em {} ms.".format(len(vector), time_in_ms))

if __name__ == '__main__':
    main()