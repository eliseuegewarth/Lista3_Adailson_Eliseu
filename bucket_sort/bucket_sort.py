def bucket_sort(vector=None):
    if len(vector) < 2:
        pass
    else:
        i = vector[len(vector)//2] # Apply M.o.M. to better performance
        first_part = []
        median_part = []
        last_part = []
        for y in vector:
            if y > i:
                last_part.append(y)
            elif y == i:
                median_part.append(y)
            else:
                first_part.append(y)
        first_part = bucket_sort(first_part)
        last_part = bucket_sort(last_part)
        vector = first_part + median_part + last_part
    return vector
