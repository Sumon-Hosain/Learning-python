import pandas as pd
var=pd.read_csv('C:\\Users\\sumon\\Downloads\\12.csv')
var1=var.dropna(axis=0)
print(var1)