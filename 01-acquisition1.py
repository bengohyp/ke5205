file = open('data/moby_dick.txt', mode='r')
#print(file.read())
print(file.closed) #False
file.close()
print(file.closed) #True
with open('data/moby_dick.txt') as file:
    print(file.readline())
with open('data/moby_dick.txt') as file:
    print(file.readline())
    book=file.readlines()
print(len(book))
import pandas as pd
file = 'data/titanic.csv'
df = pd.read_csv(file)
#print(df)
print(df.head())
import matplotlib
#pd.DataFrame.hist(df.iloc[:,4:5])
import matplotlib.pyplot as plt
plt.show()