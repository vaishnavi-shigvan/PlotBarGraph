'''
Consider the following data. Plot a bar graph. It should have the following:
a) Graph title should be “Mela Sales Report”.
b) X axis label as Days.
c) Y axis label as “Sales in Rs”.
d) Bar colors are red for week 1, blue for week 2 and brown for week3.
e) Edge color should be black
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
week1=[7500,5500,6100,4500,5700,4000,6500]
week2=[6800,4700,5700,4800,5400,2700,5900]
week3=[7100,4500,4000,3700,4000,2200,6100]
day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

plt.bar(week1,day,color="red",edgecolor="black",width=150,label="week1")
plt.bar(week2,day,color="blue",edgecolor="black",width=150,label="week2")
plt.bar(week3,day,color="brown",edgecolor="black",width=150,label="week3")

plt.legend()
plt.xlabel("Days")
plt.ylabel("Sales in Rs")
plt.title("Mela Sales Report")
plt.show()
