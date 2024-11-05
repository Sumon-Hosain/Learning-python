import pandas as pd
var=pd.read_csv('C:\\Users\\sumon\\Downloads\\data.csv')
#print(var.to_string())               # 'to_string()' for showing entire DataFrame
pd.options.display.max_columns=4     # This line for changeing   
pd.options.display.max_rows=169 
print(var)
