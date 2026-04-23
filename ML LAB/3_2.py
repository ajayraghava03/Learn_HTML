import matplotlib.pyplot as plt

import numpy as np

x_input=input("enter the x coordinate")
y_input = input("enter the y coordinate")

x = np.array([float(i) for i in x_input.split()])
y = np.array([float(i) for i in y_input.split()])

if len(x)!=len(y):
    print("The length are same ")
else:
    plt.plot(x,y,marker="o")
    plt.xlabel("hi")
    plt.ylabel("Hello")
    plt.title("home")
    plt.grid(True)
    plt.show()
    