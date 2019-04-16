import matplotlib.pyplot as plt
from gera_vector import *

def test_gera_vetor(numbers=10000000):
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
    duration['sync'] = int(1000*1000*(end - start))/1000

    r = []
    start = time.time()
    r = gera_vector_rapido([bottom_limit, top_limit], numbers)
    end=time.time()
    if len(r) != numbers:
         raise Exception("vector size ({}) is lower than number of elements ({})\n".format(len(r), numbers))
    duration['async'] = int(1000*1000*(end - start))/1000

    return duration

def plot_run_benchmark():
    x = []
    y_async = []
    y_sync = []
    start_range_size = 1000
    end_range_size = 1000000
    step_size = end_range_size//10
    for i in range(start_range_size, end_range_size+1, step_size):
        benchmark = test_gera_vetor(i)
        x.append(i)
        y_async.append(benchmark['async'])
        y_sync.append(benchmark['sync'])

    fig, ax = plt.subplots()
    ax.plot(x, y_async, '--g', label='async')
    ax.plot(x, y_sync, '-b', label='sync')

    plt.show()
