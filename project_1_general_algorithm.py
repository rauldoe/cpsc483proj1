import pandas as pd
import numpy
import math

data = pd.read_csv("project_1.csv") #read CSV file

print(data.columns)
print(data)


##a = data.iloc[:,-1].unique()[0].count(data.iloc[:,-1].unique()[0]) #tried to store the element types in a/b so for Total column, it'd be yes/no
##b = data.iloc[:,-1].unique()[1]
##print("a is: ", a)
##print("b is: ", b)
##
Entropy = [] #Created a list that will hold all our entropies

last_column = data.iloc[:,-1] #gets us the last column values

print(last_column.shape)

counter = data.iloc[:,-1].value_counts() #get us the UNIQUE values count in the last column and saves it in an array, array = [unique1, unique2,...]
print("counter is: ", counter) 

total_count = 0
for a in counter: #get us the number of times that unique value appears in the counter
    print("a is: ", a)
    total_count += a


E_S = ((-counter[0] / total_count) * math.log(counter[0]/total_count,2)) - ((counter[1]/total_count) * math.log(counter[1]/total_count,2))
print("E_S is :", E_S)
Entropy.append(E_S) #adds our E(S) entropy into the Entropy list

for b in data.columns: #A for loop that contains the 
    print("b is: ", b) #get us the unique column name 
    test = data[b].value_counts() #get us our test values for that unique column name
    print("test is: ", test) 
    
