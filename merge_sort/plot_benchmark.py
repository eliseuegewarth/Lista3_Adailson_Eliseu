import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from os import listdir
from os.path import isfile, join

def get_dataset(dataset_file_name):
    df = pd.read_csv(dataset_file_name, skipinitialspace=True)
    return df

def sort_by_columns(dataframe, columns):
    df = dataframe.sort_values(by=columns)
    return df

def plot_benchmark(dataframes, *args):
    ax = None
    if dataframes:
        pass
    elif args:
        dataframes = [x for x in args]

    for dataframe in dataframes:
        if not ax:
            ax = dataframe.plot(kind='line', x='dataset_size', y='time_in_ms', title="Sort benchmark")
            ax.set_ylabel('Time (ms)')
            ax.set_xlabel('Number of elements to sort')
        else:
            dataframe.plot(kind='line', x='dataset_size', y='time_in_ms', ax=ax)
    return ax

if __name__ == '__main__':
    files = []
    # import ipdb;ipdb.set_trace()
    if len(sys.argv) > 1:
        if sys.argv[1] == '__all__':
            mypath = "."
            extension = ".csv"
            files = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and extension in f)]
        else:
            for y in sys.argv[1:]:
                files.append(str(y))
    else:
        files.append('benchmark_recursive_merge_sort.csv')
    file_dfs = []
    df_medians = []
    for file in files:
        df_median = []
        df = get_dataset(file)
        df = sort_by_columns(df, ['dataset_size','time_in_ms'])
        for i in range(df.dataset_size.unique().size):
            median_of = "{}_median".format("_".join(file.split('_')[1:8]))
            df_median.append([median_of, df.dataset_size.unique()[i], np.median(df[df.dataset_size == df.dataset_size.unique()[i]].iloc[:,2].values), True])
        file_dfs.append(df)
        df_median = pd.DataFrame(df_median, columns=["strategy", "dataset_size", "time_in_ms", "is_random"])
        df_median = sort_by_columns(df_median, ['dataset_size','time_in_ms'])
        df_medians.append(df_median)
    dfs = file_dfs
    x_medians_meeting = 0
    y_medians_meeting = 0
    for i in range(len(df_medians[0])):
        if df_medians[0].iloc[i][2] < df_medians[1].iloc[i][2]:
            x_medians_meeting = df_medians[0].iloc[i][1]
            y_medians_meeting = df_medians[0].iloc[i][2]
            break
    ax = plot_benchmark(dataframes=dfs+df_medians)
    ax.plot(x_medians_meeting, y_medians_meeting, 'ko')
    ax.legend([df.strategy.unique()[0] for df in dfs+df_medians]+ ['crosspoint'])
    plt.show()
