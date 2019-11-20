
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

def entropy(valueCountLookup):
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
        joined = joined + str(arr[i]) + delim
    return joined

def toStringList(list):
    strList = []
    for i in list:
        strList.append(str(i))
    return strList

def unique(matrix):
    d = {}

    for i in range(0, len(matrix)):
        listKey = toStringList(matrix[i].tolist())
        key = join(listKey, '/')
        if (key in d.keys()):
            count = int(d[key]['count']) + 1
            d[key] = {'listkey' : listKey, 'count' : count}
        else:
            d.update({key : {'listkey' : listKey, 'count' : 1}})
    return d

def getLookupItem(lookup, attribute):
    list = []
    total = 0
    for i in lookup.keys():
        if (lookup[i]['listkey'][0] == attribute):
            list.append(lookup[i])
            total += int(lookup[i]['count'])
    return {'list' : list, 'total' : total}

def entropyWrt(lookupItem):
    entropy = 0.0

    total = int(lookupItem['total'])
    lookup = lookupItem['list']

    for i in lookup:
        # attribValue = i['listkey'][0]
        count = int(i['count'])
        
        p = count/total
        entropy -= p * math.log(p, 2)
    return entropy

def findMax(lookupList):
    maxItem = None

    for i in lookupList.items():
        if ((maxItem is None) or float(maxItem[1]) < float(i[1])):
            # print('setting max')
            # print(i)
            maxItem = i
    return maxItem

dependentAttribute = 'play'

os.chdir('C:/temp/cpsc483proj1')

df = pd.read_csv('tennis.csv')

rowCount = df.shape[0]
colCount = df.shape[1]
data = df.to_numpy()

attribList = df.axes[1]

fList = getFeatureList(attribList, dependentAttribute)

k1 = getValueCountLookup(df, dependentAttribute)
totalEntropy = entropy(k1)
print(totalEntropy)

igList = {}
for feature in fList:
    fm = df[feature].to_numpy()
    featureOutcomes = toStringList(np.unique(fm, return_counts=False))
    # print(featureOutcomes)
    m = df[[feature, dependentAttribute]].to_numpy()
    dict = unique(m)

    outcomeSummation = 0.0
    for outcome in featureOutcomes:
        li = getLookupItem(dict, outcome)
        pOutcome = int(li['total'])/rowCount
        e = entropyWrt(li)
        outcomeSummation -= pOutcome * e
        # print(e)

    informationGain = totalEntropy + outcomeSummation
    igList.update({ feature : informationGain})
    # print(feature + ': ' + str(informationGain))

maxItem = findMax(igList)
fList.remove(maxItem[0])

# if len(fList) > 0:
