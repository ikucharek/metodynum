# 1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)
from cs50 import get_float
from matplotlib import *
from numpy import *

def countField():
    typ=0
    while typ != 'circle' and typ != 'rectangle' and typ != 'triangle' and typ != 'rhombus':
        typ=input("Please give the type of figure (circle/rectangle/triangle/rhombus) ")
        if typ == 'circle':
            x=0
            while x <= 0:
                x = get_float("Give radius ")
                if x <= 0:
                    print("Radius must be > 0 ")
                if x > 0:
                    Field_circle = pi * x ** 2
                    print("The field is ", Field_circle)
        if typ == 'rectangle':
            x = 0
            y = 0
            while x <= 0 or y <= 0:
                x = get_float("Give 1st side ")
                y = get_float("Give 2nd side ")
                if x <= 0:
                    print("1st side must be > 0")
                if y <= 0:
                    print("2nd side must be > 0")
                if x > 0 and y > 0:
                    Field_rectangle = x * y
                    print("The field is ", Field_rectangle)
        if typ == 'triangle':
            x = 0
            y = 0
            while x <= 0 or y <= 0:
                x = get_float("Give the base ")
                y = get_float("Give the height ")
                if x <= 0:
                    print("Base must be > 0")
                if y <= 0:
                    print("Height must be > 0")
                if x > 0 and y > 0:
                    Field_triangle = x * y * 0.5
                    print("The field is ", Field_triangle)
        if typ == 'rhombus':
            x = 0
            y = 0
            while x <= 0 or y <= 0:
                x = get_float("Give the 1st diagonal ")
                y = get_float("Give the 2nd diagonal ")
                if x <= 0:
                    print("1st diagonal must be > 0")
                if y <= 0:
                    print("2nd diagonal must be > 0")
                if x > 0 and y > 0:
                    Field_rhombus = x * y * 0.5
                    print("The field is ", Field_rhombus)
        if typ!='circle' and typ!='rectangle' and typ!='triangle' and typ!='rhombus':
            print("Please give another type of figure")

countField()