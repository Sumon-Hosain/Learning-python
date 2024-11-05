import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data.csv')
new_var=var.head(50)
new_var.dropna(inplace=True)
print(new_var.to_string())