# import numpy as np
import pandas as pd
# from sklearn.model_selection import train_test_split

# changed to pandas due to performance
hist_data =pd.read_csv('train.csv', sep=',', header=None)
# HEADERS: PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

print("First row Name: " + str(hist_data.values[0][3]))

