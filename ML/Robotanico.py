#Program that predict the type of iris flower

import numpy as np 
import pandas as pd 
import seaborn as sb


df = pd.read_csv('Folders/iris.csv')

x = np.array(df.drop('target',1))
y = np.array(df.target)

#Use KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier

print("\nPredict with Neighbors")
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x,y)
predictNei = knn.predict([[6.5,6.5,4.7,1.3]])
print(predictNei)


#Use DecisionTree
from sklearn import tree

print("\nPredict with Decision Tree")
dt = tree.DecisionTreeClassifier()
dt.fit(x,y)
predictDT = dt.predict([[6.5,6.5,4.7,1.3]])
print(predictDT)