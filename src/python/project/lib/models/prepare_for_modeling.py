from sklearn.model_selection import train_test_split




def traintest_split(data):
	# Split the data into training and test sets. (0.75, 0.25) split.
	train, test = train_test_split(data)
	# The predicted column is "quality" which is a scalar from [3, 9]
	train_x = train.drop(["quality"], axis=1)
	test_x = test.drop(["quality"], axis=1)
	train_y = train[["quality"]]
	test_y = test[["quality"]]
	return train_x,test_x,train_y,test_y
	
