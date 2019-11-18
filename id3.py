
import pandas as pd
import numpy as np

dependentAttribute = 'outlook'
df = pd.read_csv('tennis.csv')

rowCount = df.shape[0]
colCount = df.shape[1]

data = df.to_numpy()

attribList = df.axes[1]

print(len(attribList))
print(attribList[0])
print(attribList[1])

rowCount = len(data[0])

dependentList = df[dependentAttribute].to_numpy()
unique_elements, counts_elements = np.unique(dependentList, return_counts=True)
countList = np.asarray((unique_elements, counts_elements))

len(df['outlook'])

a = np.array( ['YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES'] )
print("Original array:")
print(a)
unique_elements, counts_elements = np.unique(a, return_counts=True)
print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)))


def calculateEntropy(attribList, data, dependentAttribute):
    return 1