import pandas as pd
import matplotlib.pyplot as plt
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data2.csv')
var.plot(kind='scatter',x='Calories',y='Duration')
plt.show()