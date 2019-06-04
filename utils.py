import numpy as np



def wrapper(filename):
	f=open(filename)
	classes=[]
	data=[]
	for x in f.readlines():
		classes.append(x.split(',')[-1].replace('\n',''))
		dt=x.split(',')[0:-2]
		aux=[]
		for i in dt:
			aux.append(float(i))
		data.append(aux)
	data=data[0:-1]
	classes=classes[0:-1]
	setClasses=list(set(classes))
	numericalClasses=[]
	for i in classes:
		numericalClasses.append(setClasses.index(i))
	return np.array([data,classes])
	#print(setClasses)
	#print(data)
	#print(classes)
	#print(numericalClasses)

print(wrapper('bezdekIris.data').shape)