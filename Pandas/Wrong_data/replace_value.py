import pandas as pd
pd.options.display.max_rows=170
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data.csv')
var.loc[166,'Calories']=500
print(var)