import pandas as pd
var=pd.read_json('C:\\Users\\sumon\\Downloads\\1.json')
#print(var.to_string())
pd.options.display.max_columns=1000
pd.options.display.max_rows=1000
print(var)