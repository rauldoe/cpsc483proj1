
import pandas as pd
import numpy as np
import math

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
    # print(lookup)
    # print(total)

    for key in lookup:
        px = lookup[key]/total
        entropy -= px * math.log(px, 2)
    return entropy

dependentAttribute = 'play'
df = pd.read_csv('tennis.csv')

rowCount = df.shape[0]
colCount = df.shape[1]
data = df.to_numpy()

attribList = df.axes[1]

k1 = getValueCountLookup(df, dependentAttribute)

e = calculateEntropy(k1)

print(e)


