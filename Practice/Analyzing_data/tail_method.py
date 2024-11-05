import pandas as pd
var=pd.read_json('C:\\Users\\sumon\\Downloads\\1.json')
print(var.tail(10).info())