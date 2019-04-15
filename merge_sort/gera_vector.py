import random
import multiprocessing

def gera_vector(int_range, count, return_dict=None, cpu_id=None):
    vector = []
    if return_dict != None:
        return_dict[cpu_id] = [random.randint(int_range[0], int_range[1]) for x in range(count)]
    else:
        vector = [random.randint(int_range[0], int_range[1]) for x in range(count)]
    return vector

def gera_vector_rapido(int_range, count):
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    cpu_count = multiprocessing.cpu_count()
    jobs = []
    count_slice = count//cpu_count
    for i in range(cpu_count-1):
        p = multiprocessing.Process(target=gera_vector, args=(int_range, count_slice, return_dict, i))
        p.start()
        jobs.append(p)
    p = multiprocessing.Process(target=gera_vector, args=(int_range, count-((cpu_count-1)*count_slice), return_dict, cpu_count-1))
    p.start()
    jobs.append(p)

    for job in jobs:
        job.join()
    vector = []
    for i in range(cpu_count):
        for j in return_dict[i]:
            vector.append(j)

    return vector
