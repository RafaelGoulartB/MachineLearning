# Packages for analysis
import pandas as pd
import numpy as np
from sklearn import svm

recipes = pd.read_csv('Iso-vs-Con.csv')


#Specific input models
ingredients = recipes[['Carb','Protein']].as_matrix() #Creat a list sorted with Carb and Protein
type_label = np.where(recipes['Type']=='Concentrado', 0, 1) #If Type == Concentrado add 0 else add 1

#Fit the model
model = svm.SVC(kernel='linear')
model.fit(ingredients, type_label)

# Create a function to guess when a whey isolado or concentrado
def concentrado_or_isolado(carb, protein):
    if(model.predict([[carb, protein]]))==0:
        print("\nIt's a whey Concentrado")
    else:
        print("\nIt's a whey Isolado")

carb = float(input("How many Carb has in your whey? "))
prot = float(input("How many Protein has in your whey? "))
concentrado_or_isolado(carb, prot)