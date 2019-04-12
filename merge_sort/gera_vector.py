import random
import multiprocessing
import matplotlib.pyplot as plt

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

def single_run_benchmark(numbers=10000000):
    import time
    duration = {}
    numbers = int(numbers)
    top_limit = numbers*10
    bottom_limit = 0
    r = []
    start = time.time()
    r = gera_vector([bottom_limit, top_limit], numbers)
    end=time.time()
    if len(r) != numbers:
         raise Exception("vector size ({}) is lower than number of elements ({})\n".format(len(r), numbers))
    duration['sync'] = (end - start)

    r = []
    start = time.time()
    r = gera_vector_rapido([bottom_limit, top_limit], numbers)
    end=time.time()
    if len(r) != numbers:
         raise Exception("vector size ({}) is lower than number of elements ({})\n".format(len(r), numbers))
    duration['async'] = (end - start)

    return duration

def plot_run_benchmark():
    x = []
    y_async = []
    y_sync = []
    for i in range(1000, 10000000, 1000000):
        benchmark = single_run_benchmark(i)
        x.append(i)
        y_async.append(benchmark['async'])
        y_sync.append(benchmark['sync'])

    fig, ax = plt.subplots()
    ax.plot(x, y_async, '*g', label='async')
    ax.plot(x, y_sync, '-b', label='sync')

    plt.show()
