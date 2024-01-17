#%%
import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [350,330,310,310,290,270,250,265,270,270,325,326,328,329,340,340,345,350]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 22, 100)
viteza = mymodel(17)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
print(viteza)
# %%
