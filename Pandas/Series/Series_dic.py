import pandas as pd
dic={
    "name":['python','c','c++','java'],
    "Por":[12,13,14],
    'rank':[1,4,3,2]
}
var1=pd.Series(dic,index=[1,2,3,4])

print(var1)