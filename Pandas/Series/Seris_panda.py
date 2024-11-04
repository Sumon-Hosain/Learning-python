'''import pandas as pd
x=[2,3,4]
y=pd.Series(x,index=['a','b','c'],dtype='float',name='pyt')
print(y)


dic={
    "name":['python','c','c++','java'],
    "Por":[12,13,14],
    'rank':[1,4,3,2]
}
var1=pd.Series(dic,index=[1,2,3])

print(var1)'''


import pandas as pd
c=pd.Series(12,index=['1','2','3','4','5'])
d=pd.Series(10,index=['1','2','3'])
print(c+d)