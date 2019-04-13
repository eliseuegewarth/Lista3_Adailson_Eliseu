
def clear_file(benchmark_file_path):
    with open(benchmark_file_path, "w+") as file:
        file.write("{}, {}, {}, {}\n".format("strategy", "dataset_size", "time_in_ms", "is_random"))

def write(benchmark_file_path, dataset=[]):
    if dataset != []:
        with open(benchmark_file_path, "a+") as file:
            for i in dataset:
                file.write("{}, {}, {}, {}\n".format(i[0], i[1], i[2], i[3]))
