import time
import sys
from gera_vector import gera_vector_rapido
from benchmark import *
from recursive_merge_sort import recursive_merge_sort

def single_run(sort_strategy=recursive_merge_sort, sort_strategy_name='recursive_merge_sort', number_of_elements=100000, start_of_range=0, end_of_range=1000000):
    vector = gera_vector_rapido([start_of_range, end_of_range], number_of_elements)
    start = time.time()
    vector = sort_strategy(vector)
    end = time.time()
    time_in_ms = (int(1000*1000*(end-start)))/1000
    return [sort_strategy_name, len(vector), time_in_ms, True]

def run_benchmark(sort_strategy=recursive_merge_sort, sort_strategy_name='recursive_merge_sort', iterations_per_benchmark=100, start_with_n_elements=100, end_with_n_elements=100000, range_step=10000, new_benchmark=False):
    benchmark_file_path = "benchmark_merge_sort{}_{}.csv".format(start_with_n_elements, end_with_n_elements)
    if new_benchmark:
        clear_benchmark_file(benchmark_file_path)
    else:
        pass
    start_with_n_elements = int(start_with_n_elements)
    end_with_n_elements = int(end_with_n_elements)
    range_step = int(range_step)
    if end_with_n_elements < start_with_n_elements:
        raise Exception("\nEnd must be greater than start.\n")
    elif range_step >= (end_with_n_elements-start_with_n_elements) :
        raise Exception("\nThe step range be in [start-end] interval.\n")
    for number_of_elements in range(start_with_n_elements, end_with_n_elements, range_step):
        for i in range(int(iterations_per_benchmark)):
            benchmark = single_run(sort_strategy, sort_strategy_name, number_of_elements)
            write_benchmark(
                benchmark_file_path,
                benchmark[0],
                benchmark[1],
                benchmark[2],
                benchmark[3],
                )

def main():
    print('Deseja:\n1) Realizar uma analise de performance\n2) Executar o algoritmo apenas uma vez?\n')
    opcao = int(input(''))
    if opcao == 1:
        # some other inputs
        pass
    else:
        elementos = int(input("Deseja ordenar quantos elementos?"))
        benchmark = single_run()
        print("{} elementos em {} ms".format(benchmark[1], benchmark[2]))

if __name__ == '__main__':
    if (len(sys.argv) == 7):
        if sys.argv[1] == 'recursive_merge_sort':
            run_benchmark(recursive_merge_sort, "recursive_merge_sort", sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], False)
        elif sys.argv[1] == 'iterative_merge_sort':
            # run_benchmark(iterative_merge_sort, "iterative_merge_sort", sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], False)
            pass
        else:
            pass
    else:
        main()
