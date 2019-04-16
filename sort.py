#!/bin/python3
import time
import sys
from os.path import isfile
from gera_vector import gera_vector_rapido
import benchmark
from merge_sort.recursive_merge_sort import recursive_merge_sort as merge_sort
from merge_sort.parallel_merge_sort import parallel_merge_sort

def run_test(sort_strategy=merge_sort, sort_strategy_name='merge_sort', number_of_elements=100000, start_of_range=0, end_of_range=1000000):
    vector = gera_vector_rapido([start_of_range, end_of_range], number_of_elements)
    start = time.time()
    vector = sort_strategy(vector)
    end = time.time()
    time_in_ms = (int(1000*1000*(end-start)))/1000
    return [sort_strategy_name, len(vector), time_in_ms, True]

def run_benchmark(sort_strategy=merge_sort, sort_strategy_name='merge_sort', iterations_per_benchmark=100, start_with_n_elements=100, end_with_n_elements=100000, range_step=10000, new_benchmark=False):
    benchmark_file_path = "tests_{}_{}_{}.csv".format(sort_strategy_name, start_with_n_elements, end_with_n_elements)
    if new_benchmark or not isfile(benchmark_file_path):
        benchmark.clear_file(benchmark_file_path)
    else:
        pass
    start_with_n_elements = int(start_with_n_elements)
    end_with_n_elements = int(end_with_n_elements)
    range_step = int(range_step)
    if end_with_n_elements < start_with_n_elements:
        raise Exception("\nEnd must be greater than start.\n")
    elif range_step >= (end_with_n_elements-start_with_n_elements) :
        raise Exception("\nThe step range be in [start-end] interval.\n")
    for i in range(int(iterations_per_benchmark)):
        tests = []
        for number_of_elements in range(start_with_n_elements, end_with_n_elements+1, range_step):
            single_test = run_test(sort_strategy, sort_strategy_name, number_of_elements)
            tests.append(single_test)
        benchmark.write(
                benchmark_file_path,
                tests
                )

def main():
    print('Deseja:\n1) Realizar uma analise de performance\n2) Executar o algoritmo apenas uma vez?\n')
    opcao = int(input(''))
    if opcao == 1:
        # some other inputs
        pass
    else:
        elementos = int(input("Deseja ordenar quantos elementos?"))
        single_test = run_test(number_of_elements=elementos)
        print("{} elementos em {} ms".format(single_test[1], single_test[2]))

if __name__ == '__main__':
    if (len(sys.argv) >= 6):
        if sys.argv[1] == 'recursive_merge_sort':
            run_benchmark(merge_sort, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], True if sys.argv[6] == "True" else False)
        elif sys.argv[1] == 'parallel_merge_sort':
            run_benchmark(parallel_merge_sort, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], True if sys.argv[6] == "True" else False)
        elif sys.argv[1] == 'iterative_merge_sort':
            # run_benchmark(iterative_merge_sort, "iterative_merge_sort", sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], False if sys.argv[6] == "False" else True)
            pass
        else:
            pass
    elif(len(sys.argv) == 2):
        if sys.argv[1] == "--test":
            single_test = run_test(number_of_elements=100000)
            print("{} elementos em {} ms".format(single_test[1], single_test[2]))
        elif sys.argv[1] == "--get-info":
            main()
        elif sys.argv[1] == "--help":
            print("USAGE:\n\t{} <sort_strategy> <iterations_per_benchmark> <start_with_n_elements> <end_with_n_elements> <range_step> <new_benchmark>".format(sys.argv[0]))
    else:
        print("USAGE:\n\t{} <sort_strategy> <iterations_per_benchmark> <start_with_n_elements> <end_with_n_elements> <range_step> <new_benchmark>".format(sys.argv[0]))
