import pandas as pd
pd.options.display.max_rows=200
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data.csv')
var.loc[168,'Calories'] = 500
for x in var.index:
    if var.loc[x,'Calories']>100:
        var.drop(x,inplace=True)
print(var)