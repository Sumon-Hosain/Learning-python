import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data.csv')
pd.options.display.max_rows=200
var.loc[166,'Calories']=5000
for x in var.index:
    if var.loc[x,'Calories']>500:
        var.drop(x,inplace=True)
print(var)