import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

X=np.array([
    [1000,2,5],
    [1500,3,10],
    [1800,4,8],
    [1200,2,6],
    [2000,5,12]
])
y=np.array([300000,400000,500000,320000,600000])

model=LinearRegression()

model.fit(X,y)

yp=model.predict(X)

NH=np.array([[1600,3,7]])
print("Predict Price :",model.predict(NH)[0])

plt.scatter(y,yp)
plt.xlabel("Actual price")
plt.ylabel("Predicted Price")
plt.title("pridect home price ")
plt.show()