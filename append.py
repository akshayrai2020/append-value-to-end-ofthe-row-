import pandas as pd
import csv
import os


filepath = r"D:\nse\NSEdaily\Old folder\1234MTO_17122019DAT.csv"
exitFolder = r"D:\nse\NSEdaily\Old folder"
df = pd.read_csv(filepath)
for i in df.index:

    name = df['Name of Security'][i]+".csv"
    addColumn = df['% of Deliverable Quantity to Traded Quantity'][i]

    if os.path.isfile(exitFolder+"\\"+name):
        print("File exist")
        df1 = pd.read_csv(exitFolder+"\\"+name)

        fileHandle = open(exitFolder+"\\"+name, 'r')
        lineList = fileHandle.readlines()

        last = lineList.pop()
        lastRow = str(last)
        lastRow = lastRow.strip('\n')+","+str(addColumn)
        print(lastRow)
        lineList.append(lastRow)
        f = open(exitFolder+"\\"+name, "w+")
        f.writelines(lineList)
    else:
        print("File not exist")
        print("append complete")
