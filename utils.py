import numpy as np


# Method for wrapping a file in UCI format:
#   Instance: [a_1,a_2, ..., a_n, class]
# The filename is in the next format:
#   a_1, a_2, ..., a_n, class => class name as a string
# Input: the path to the file that has the dataset
# Return: a numpy array with the data and the classes [data, classes]
def wrapper(filename):
	f=open(filename)
	#list for the classes and the data
	classes=[]
	data=[]
	#Read the lines in the file
	for x in f.readlines():
		# separe to get a list, the separator is ','
		# the classes are in the last position, and the
		# data in the first k positions
		classes.append(x.split(',')[-1].replace('\n',''))
		dt=x.split(',')[0:-2]
		# here we convert the data into float values 
		aux=[]
		for i in dt:
			aux.append(float(i))
		data.append(aux)
	# I don't know why, but the last value is an empty list,
	# so I remove from the data and classes list
	data=data[0:-1]
	classes=classes[0:-1]
	# A set haven't the same values, so we conver the classes
	# into a set and we convert the classses to int values with
	# the position of that class in a set
	setClasses=list(set(classes))
	numericalClasses=[]
	for i in classes:
		numericalClasses.append(setClasses.index(i))
	# The return is a numpy array with the data and the
	# corresponding classes
	return np.array([data,numericalClasses])

print(wrapper('bezdekIris.data').shape)