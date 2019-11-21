
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

def getFeatureList(attributeList, decisionAttribute):
    return [i for i in attributeList if i != decisionAttribute]

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
    maxItem = ('', 0.0)

    for i in lookupList.items():
        if (float(maxItem[1]) < float(i[1])):
            # print('setting max')
            # print(i)
            maxItem = i
    return maxItem

def computeInformationGain(df1, decisionAttribute, fList):
    igList = {}

    rowCount = df1.shape[0]

    k1 = getValueCountLookup(df1, decisionAttribute)
    totalEntropy = entropy(k1)
    # print(f'Total Entropy: {totalEntropy}')

    if (totalEntropy == 0.0):
        informationGain = 0.0
    else:
        for feature in fList:
            fm = df1[feature].to_numpy()
            featureOutcomes = toStringList(np.unique(fm, return_counts=False))
            # print(featureOutcomes)
            m = df1[[feature, decisionAttribute]].to_numpy()
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

    return igList

def getID3Node(df, fList, feature, outcomes):

    if len(fList) > 1:

        for outcome in outcomes:
            # print(f"{feature} == '{parentOutCome0}'")
            subDf = df.query(f"{feature} == '{outcome}'")
            
            igList = computeInformationGain(subDf, decisionAttribute, fList)
            if (len(igList.items()) > 0):
                maxItem = findMax(igList)
                maxItemFeature = maxItem[0]
                print(f'max: {maxItemFeature}')
                maxItemOutcomes = toStringList(np.unique(subDf[feature].to_numpy(), return_counts=False))
                fList.remove(maxItemFeature)
                print(fList)

                getID3Node(subDf, fList, maxItemFeature, maxItemOutcomes)

os.chdir('C:/temp/cpsc483proj1')

decisionAttribute = 'play'
df = pd.read_csv('tennis.csv')
fList = getFeatureList(df.axes[1], decisionAttribute)

igList0 = computeInformationGain(df, decisionAttribute, fList)
maxItem0 = findMax(igList0)
parent0 = maxItem0[0]
parentOutComes0 = toStringList(np.unique(df[parent0].to_numpy(), return_counts=False))
fList.remove(parent0)

getID3Node(df, fList, parent0, parentOutComes0)

# if len(fList) > 1:

#     for parentOutCome0 in parentOutComes0:
#         # print(f"{parent0} == '{parentOutCome0}'")
#         df0 = df.query(f"{parent0} == '{parentOutCome0}'")
        
#         igList1 = computeInformationGain(df0, decisionAttribute, fList)
#         if (len(igList1.items()) > 0):
#             maxItem1 = findMax(igList1)
#             parent1 = maxItem1[0]
#             print(f'max: {parent1}')
#             parentOutComes1 = toStringList(np.unique(df0[parent1].to_numpy(), return_counts=False))
#             fList.remove(parent1)
#             print(fList)

#             if len(fList) > 1:

#                 for parentOutCome1 in parentOutComes1:
#                     print(f"{parent1} == '{parentOutCome1}'")
#                     df1 = df0.query(f"{parent1} == '{parentOutCome1}'")
                    
#                     igList2 = computeInformationGain(df1, decisionAttribute, fList)
#                     if (len(igList2.items()) > 0):
#                         maxItem2 = findMax(igList2)
#                         parent2 = maxItem2[0]
#                         print(f'max: {parent2}')
#                         parentOutComes2 = toStringList(np.unique(df1[parent2].to_numpy(), return_counts=False))
#                         fList.remove(parent2)

