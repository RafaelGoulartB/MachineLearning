from sklearn import tree

features = [[140, 1],[130, 1],[150, 0],[170, 0]] #0- bumpy, 1- smooth
labels = [0, 0, 1, 1] #0 - apple, 1- oranges

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

try:
	surface = int(input("\nThe fruit surface is bumpy or smooth?[1-Smooth 0-Bumpy] "))
	weight = int(input("What's the fruit's weight? "))

except ValueError:
	print("Write a number 1 or 0.")

predict = clf.predict([[weight, surface]])
if predict == 0:
	print("\nThis fruit is an apple.")

elif predict == 1:
	print("\nThis fruit is an orange.")
