import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch date and format it
data = fetch_movielens(min_rating=4.0) #Data is a CSV file that contens movies

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#Create model
model = LightFM(loss='warp')
#Train model
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
	#Number of users and movies in traing data
	n_users, n_items = data['train'].shape

	#Generate recommendations for each user we input
	for user_id in user_ids:
		#Movies they already like
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
		#Movies our model predicts they will like
		scores = model.predict(user_id, np.arange(n_items))
		#Rank them in order of most liked to least
		top_items = data['item_labels'][np.argsort(-scores)]

		#Print Out the  results
		print("Users {}".format(user_id))
		print("		Know positives:")

		for x in known_positives[:3]:
			print("		{}".format(x))
		print("		Recommended:")

		for x in top_items[:5]:
			print("		{}".format(x))

sample_recommendation(model, data, [1, 2, 500])
