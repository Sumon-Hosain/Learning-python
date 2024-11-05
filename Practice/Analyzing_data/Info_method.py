import pandas as pd
var=pd.read_csv('C:\\Users\\sumon\\Downloads\\data.csv')
pd.options.display.max_rows=200
pd.options.display.max_columns=5
print(var.info())