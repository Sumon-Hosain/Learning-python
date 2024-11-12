import pandas as pd
import matplotlib.pyplot as plt
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data1.csv')
var['Calories'].plot(kind='hist')
plt.show()