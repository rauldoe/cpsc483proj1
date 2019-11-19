
import pandas as pd
import numpy as np
import math
import os

def getValueCountLookup(dataFrame, attributeName):
    total = 0
    keyLookup = {}
    dependentList = dataFrame[attributeName].to_numpy()
    keyList, countList = np.unique(dependentList, return_counts=True)

    for i in range(0, len(keyList)):
        total += countList[i]
        keyLookup.update({keyList[i] : countList[i]})

    return {'lookup' : keyLookup, 'total' : total}

def getFeatureList(attributeList, dependentAttribute):
    return [i for i in attributeList if i != dependentAttribute]

def calculateEntropy(valueCountLookup):
    entropy = 0.0
    lookup = valueCountLookup['lookup']
    total = valueCountLookup['total']

    for key in lookup:
        px = lookup[key]/total
        entropy -= px * math.log(px, 2)
    return entropy

def join(arr, delim):
    joined = ''
    for i in range(0, len(arr)):
        joined = joined + arr[i] + delim
    return joined

dependentAttribute = 'play'

os.chdir('C:/temp/cpsc483proj1')

df = pd.read_csv('tennis.csv')

rowCount = df.shape[0]
colCount = df.shape[1]
data = df.to_numpy()

attribList = df.axes[1]

k1 = getValueCountLookup(df, dependentAttribute)
e = calculateEntropy(k1)
print(e)


m = df[['outlook', 'play']].to_numpy()
dict = {}

for i in range(0, len(m)):
    val = m[i]
    key = join((m[i]).tolist(), '/')
    if (key in dict.keys()):
        count = dict[key]['count']
        dict[key] = count + 1
    else:
        dict[key] = 1
# df[['outlook', 'play']].groupby(['outlook']).count()

print(dict)