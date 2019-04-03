
def clear_benchmark_file(benchmark_file_path):
    with open(benchmark_file_path, "w+") as file:
        file.write("{}, {}, {}, {}\n".format("strategy", "dataset_size", "time_in_ms", "is_random"))

def write_benchmark(benchmark_file_path, strategy, dataset_size, time_in_ms, is_random=True):
    with open(benchmark_file_path, "a+") as file:
        file.write("{}, {}, {}, {}\n".format(strategy, dataset_size, time_in_ms, is_random))
