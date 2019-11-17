import math
import numpy
import pandas as pd

data = pd.read_csv("project_1.csv") #read CSV file

len_of_columns = len(data.columns) # gets the numbers of columns in the csv
print(len_of_columns)
print(data.columns)


a = data.iloc[:,-1].unique()[0].count(data.iloc[:,-1].unique()[0]) #tried to store the element types in a/b so for Total column, it'd be yes/no
b = data.iloc[:,-1].unique()[1]
print("a is: ", a)
print("b is: ", b)

print("initial statement is 6 leave-alone and 4 force-into")
print ("For to get E(S), we use -P(x)logbase2P(X)")
print("E(S) is: -6/10 * logbase2(9/14) - 4/10 logbase2(4/10)")
print("E(S) = ", (-.6 * math.log(6/10,2))- (4/10 * math.log(4/10,2)))

