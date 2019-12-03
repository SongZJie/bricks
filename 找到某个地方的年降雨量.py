import pandas as pd
import csv
import os
import csv
import sys



path = pd.read_excel(r"C:\Users\Song\Desktop\56-20jiangshui.xlsx",header=None)

global data
data = []
for i in range(31594):
    if path.iloc[i, 0] == 52889:
        data.append(path.iloc[i])

csvFile2 = open('C:/Users/Song/Desktop/result2.csv', 'w')#mode要写成wb,如果是w，则会出现空行的情况。
writer = csv.writer(csvFile2)

m = len(data)
for i in range(m):
    writer.writerow(data[i])



#writer.writerow(newTitle)
csvFile2.close()






