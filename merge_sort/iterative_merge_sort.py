
def iterative_merge_sort(vector):
    vector_size = len(vector)
    slot_size = 1
    slot_distance = 2*slot_size
    while(slot_size <= vector_size):
        vector = swap_merge(vector, slot_size, slot_distance)
        slot_size = slot_size + 1
        slot_distance = 2*slot_size
    return vector

def swap_merge(vector, slot_size, slot_distance):
    slots = len(vector)//slot_distance + 1 if (len(vector)/slot_distance - len(vector)//slot_distance) > 0 else 0
    for i in range(slots):
        firt_origin = i
        second_origin = i*slot_distance
        if vector[second_origin-1] <= vector[second_origin]:
            pass
        else:
            while(firt_origin < i+slot_size or second_origin < (slot_distance*i)+slot_size):
                if(firt_origin < i+slot_size and second_origin < (slot_distance*i)+slot_size):
                    if vector[firt_origin] > vector[second_origin]:
                        print("Swap {} and {}\n".format(vector[firt_origin], vector[second_origin]))
                        swap = vector[firt_origin]
                        vector[firt_origin] = vector[second_origin]
                        vector[second_origin] = swap
                        firt_origin += 1
                    else:
                        second_origin += 1
    return vector
