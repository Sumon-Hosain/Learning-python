import pandas as pd
a={
    "A":[1,2,4],
    "B":[1,1,3]
}
var=pd.DataFrame(a)
print(var.loc[0])