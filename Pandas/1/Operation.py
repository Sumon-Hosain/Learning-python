import pandas as pd
var={
    'A':[10,20,30,40],
    'B':[50,60,70,80]
}
var1=pd.DataFrame(var)
var1['Python2'] = var1['B'] >= 55
var1['Python'] = var1['A'] <= 15
print(var1)