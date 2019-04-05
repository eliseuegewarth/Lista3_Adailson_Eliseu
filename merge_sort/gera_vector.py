import random

def gera_vector(int_range, count):
    return [random.randint(int_range[0], int_range[1]) for x in range(count)]