from cs50 import get_int
from matplotlib import *
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

# TASKS (8p)- calculate & print:
# 0 Use alternative way of reading inputs - using library (0.5p)
x = get_int("x: ")
y = get_int("y: ")

# 1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
k = 5
l = 2


def poleobw(x, y):
    p1 = pi * x ** 2
    p2 = pi * y ** 2
    o1 = 2 * pi * x
    o2 = 2 * pi * y
    print('pole 1 =', p1, 'pole 2 =', p2, 'obw1 =', o1, 'obw2 = ', o2)


poleobw(l, k)

# 2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
xx = arange(2, 50)
yy = arange(2, 50)

for i in range(0, len(xx)):
    for j in range(1, len(xx)):
        if xx[i] % yy[j] == 0 and xx[i] % 2 == 0 and yy[j] % 2 == 0 and xx[i] != yy[j]:
            print(yy[j], xx[i])

# 3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
x = 4
y = 2
xIsEven = x % y == 0
xIsEvenLog = 'X is divisible by Y' if xIsEven else 'X is not divisible by Y'
print(xIsEvenLog)

# 4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)

x = 33
y = 8
c = x / y
c = round(c, 2)
print(c)

# 5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)

k=input("Give a number (0-100, use dots if there are any decimal places) ")
try:
    k=float(k)
    if k>100:
        print("Give a number (0-100, use dots if there are any decimal places)!!! ")
    else:
        k=round(k,0)
        k=int(k)

        xx=linspace(-1*k,10,k)
        yy=linspace(-1*k,10,k)
        x,y=meshgrid(xx,yy)
        z=x**2+x*y**2+y**3
        ax=Axes3D(figure())
        ax.plot_surface(x,y,z, cmap=cm.rainbow)
        show()
except ValueError:
    print("Give a number (0-100, use dots if there are any decimal places)!!! ")

# 6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)
