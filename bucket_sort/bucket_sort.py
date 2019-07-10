def bucket_sort(vector=None, key = lambda x:x):
    if len(vector) < 2:
        pass
    else:
        i = vector[len(vector)//2] # Apply M.o.M. to better performance
        first_part = []
        median_part = []
        last_part = []
        for y in vector:
            if key(y) > key(i):
                last_part.append(y)
            elif key(y) == key(i):
                median_part.append(y)
            else:
                first_part.append(y)
        first_part = bucket_sort(first_part, key)
        last_part = bucket_sort(last_part, key)
        vector = first_part + median_part + last_part
    return vector
