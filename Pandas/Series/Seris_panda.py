import pandas as pd
x=[2,3,4]
y=pd.Series(x,index=['a','b','c'],dtype='float',name='pyt')
print(y)
import pandas as pd
c=pd.Series(12,index=['1','2','3','4','5'])
d=pd.Series(10,index=['1','2','3'])
print(c+d)