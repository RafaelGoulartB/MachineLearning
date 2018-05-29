from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier

#[height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
'female', 'male', 'male']

class main(object):
	def __init__(self):
		global X, Y
		self.RorP = str(input("Do you wanna predict or register new informations? [P/R] ")).strip().lower()[0]
		self.height = str(input("\nWhat's your height? "))
		self.weight = str(input("What's your weight? "))
		self.shoe_size = str(input("What's your shoes size? "))
		if self.RorP == 'p':
			self.predictTree()
			self.predictKNN()
		elif self.RorP == 'r':
			self.gender = str(input("What's gender? [M/F] ")).strip().lower()[0]
			if self.gender == 'm':
				Y.append('male')
				X.append([self.height, self.weight, self.shoe_size])
			elif self.gender == 'f':
				Y.append('female')
				X.append([self.height, self.weight, self.shoe_size])
			else:
				raise ValueError
		else:
			raise ValueError

	def predictTree(self):
		'''Predict With Decision Tree'''
		self.clf = tree.DecisionTreeClassifier()
		self.clf.fit(X,Y)
		self.predict_tree = self.clf.predict([[self.height, self.weight, self.shoe_size]])
		print(self.predict_tree, "\nPrediction with Decision Tree\n")
	def predictKNN(self):
		'''Predict with neighbors'''
		self.knn = KNeighborsClassifier(n_neighbors = 5)
		self.knn.fit(X,Y)
		self.predict_knn = self.knn.predict([[self.height,self.weight, self.shoe_size]]) 
		print(self.predict_knn, '\nPrediction with neighbors')

main()