import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,6]})
#Var.insert(position of colum,Colum name,value)
#inserting
var.insert(1,"C",[10,11,12,13,14])
var["Python"] = var['B'][:3]
print(var)
#deleting 
var.pop("C")
del var["Python"]
print(var)
