import pandas as pd


def download_raw_data(save=False):
	# Read the wine-quality csv file from the URL
	csv_url =\
	'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
	try:
		data = pd.read_csv(csv_url, sep=';')
	except Exception as e:
		logger.exception(
		"Unable to download training & test CSV, check your internet connection. Error: %s", e)

	if save==True:	
		data.to_csv('data/raw/winequality-red.csv',index=False)
	return data


def read_raw_data():
	return data.read_csv('data/raw/winequality-red.csv')
