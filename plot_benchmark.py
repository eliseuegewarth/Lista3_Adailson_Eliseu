import matplotlib.pyplot as plt
import pandas as pd

def get_dataset(dataset_file_name):
	df = pd.read_csv(dataset_file_name, skipinitialspace=True)
	return df

def sort_by_columns(dataframe, columns):
	# import ipdb;ipdb.set_trace()
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
			ax = dataframe.plot(kind='line', x='dataset_size', y='time_in_ms', legend=False)
		else:
			dataframe.plot(kind='line', x='dataset_size', y='time_in_ms', legend=False, ax=ax)
	plt.show()

if __name__ == '__main__':
	df = get_dataset('benchmark_merge_sort.csv')
	df = sort_by_columns(df, ['dataset_size','time_in_ms'])
	dfs = []
	slice_in = len(df)//1000
	for i in range(slice_in):
		slice_limit = (len(df)//slice_in)
		dfs.append(df.iloc[i*slice_limit:(i+1)*slice_limit, :])
	plot_benchmark(dataframes=dfs)