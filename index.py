import numpy as np
# from sklearn.model_selection import train_test_split

hist_data = np.genfromtxt('train.csv', delimiter=',', dtype=None)
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

print(hist_data[0])