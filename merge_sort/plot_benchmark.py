import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

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
			dataframe.plot(kind='line', x='dataset_size', y='time_in_ms', legend=False, ax=ax)
	return ax

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1]:
			file = sys+argv[1]
	else:
		file = 'benchmark_recursive_merge_sort.csv'
	df = get_dataset(file)
	df = sort_by_columns(df, ['dataset_size','time_in_ms'])
	df_median = []
	for i in range(df.dataset_size.unique().size):
		df_median.append(['recursive_merge_sort', df.dataset_size.unique()[i], np.median(df[df.dataset_size == df.dataset_size.unique()[i]].iloc[:,2].values), True])
	df_median = pd.DataFrame(df_median, columns=["strategy", "dataset_size", "time_in_ms", "is_random"])
	dfs = []
	# import ipdb;ipdb.set_trace()
	slice_in = len(df)//1000
	for i in range(slice_in):
		slice_limit = (len(df)//slice_in)
		dfs.append(df.iloc[i*slice_limit:(i+1)*slice_limit, :])
	ax = plot_benchmark(dataframes=dfs)
	df_median.plot(kind='line', x='dataset_size', y='time_in_ms', color='k', ax=ax)
	plt.xticks([x for x in range(0, int(df.dataset_size.unique()[-1]*1.1), 10000)])
	plt.show()
