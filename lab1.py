
# coding: utf-8

# In[ ]:


from matplotlib import *
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

#TASKS (4p)
#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)

l=[]
for i in range(56,100):
    y = 2*i**2 + 2*i + 2
    l.append(y)
print(l)




#2 ask the user for a number and print its factorial (1p)

o=input("Please give a number ")
o=int(o)
def factorial(x):
    if x>1:
        w=factorial(x-1)*x
        return w
    else:
        return 1
factorial(o)





#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)

s=randn(10)
print(s)
def lowv(m):
    b=0
    bb=0
    for j in range(0, len(m)):
        bb=bb+1
        if m[j]>b:
            b=m[j]
    print(b, "index", bb)      
lowv(s)





#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.

n=input("Please give the length of plot ")
n=int(n)+1
ll=zeros(n)
for v in range(0, n):
    ll[v] = v**2 - sin(v/9)
plot(ll)
show()
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)


#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)
#Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.

