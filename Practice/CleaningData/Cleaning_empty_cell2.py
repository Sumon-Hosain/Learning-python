import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data.csv')
new_var=var.head(100)
pd.options.display.max_rows=105
new_var.dropna(inplace=True)
print(new_var)