import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data1.csv')
pd.options.display.max_rows=1000
print(var.corr())
