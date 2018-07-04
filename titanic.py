import pandas as pd
import numpy as np
import plt as plt

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

print(train_data.head())
##print(train_data.info())
##print(train_data.describe())
print(train_data.describe(include=['O']))

train_data = train_data.drop(labels=['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
test_data = test_data.drop(labels=['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
print(train_data.head()) # check everything looks okay

##plt.title("Distribution of Survival, (1 = Survived)")