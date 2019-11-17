
import pandas as pd
import numpy as np


df = pd.read_csv('tennis.csv')

data = df.to_numpy()

print(data)

attribList = df.axes[1]

print(len(attribList))
print(attribList[0])
print(attribList[1])


