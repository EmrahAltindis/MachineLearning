import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv("M001\\linear.csv")  # Verimizi okuyalım

x = data["metrekare"]
y = data["fiyat"]

x = np.array(x)
y = np.array(y)

a,b,c,d = np.polyfit(x,y,3)


z = np.arange(150)

plt.scatter(x,y)

plt.plot(z,a*z*z*z+b*z*z+c*z+d)


z = int(input("metrekare="))
sonuc = a*z**3+b*z**2+c*z+d
print(sonuc)

plt.scatter(z,sonuc,c="red",marker=">")
plt.show()