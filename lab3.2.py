#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
from cs50 import get_float
from matplotlib import *
from numpy import *


def compare_fields():
    Names=[]
    Fields=[]
    typ1=0
    while typ1 != 'circle' and typ1 != 'rectangle' and typ1 != 'triangle' and typ1 != 'rhombus':
        typ1 = input("Please give the type of 1st figure (circle/rectangle/triangle/rhombus) ")
        Names.append(typ1)
        if typ1 == 'circle':
            x=0
            while x<=0:
                x = get_float("Give radius ")
                if x <= 0:
                    print("Radius must be > 0 ")
                if x > 0:
                    Field_circle = pi * x ** 2
                    Fields.append(Field_circle)
        if typ1 == 'rectangle':
            x=0
            y=0
            while x<=0 or y<=0:
                x = get_float("Give 1st side ")
                y = get_float("Give 2nd side ")
                if x <= 0:
                    print("1st side must be > 0")
                if y <= 0:
                    print("2nd side must be > 0")
                if x > 0 and y > 0:
                    Field_rectangle = x * y
                    Fields.append(Field_rectangle)
        if typ1 == 'triangle':
            x=0
            y=0
            while x<=0 or y<=0:
                x = get_float("Give the base ")
                y = get_float("Give the height ")
                if x <= 0:
                    print("Base must be > 0")
                if y <= 0:
                    print("Height must be > 0")
                if x > 0 and y > 0:
                    Field_triangle = x * y * 0.5
                    Fields.append(Field_triangle)
        if typ1 == 'rhombus':
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
                    Fields.append(Field_rhombus)
        if typ1 != 'circle' and typ1 != 'rectangle' and typ1 != 'triangle' and typ1 != 'rhombus':
            print("Please give another type of figure")
            Names.remove(typ1)

    typ2 = 0
    while typ2 != 'circle' and typ2 != 'rectangle' and typ2 != 'triangle' and typ2 != 'rhombus':
        typ2 = input("Please give the type of 2nd figure (circle/rectangle/triangle/rhombus) ")
        Names.append(typ2)
        if typ2 == 'circle':
            x = 0
            while x <= 0:
                x = get_float("Give radius ")
                if x <= 0:
                    print("Radius must be > 0 ")
                if x > 0:
                    Field_circle = pi * x ** 2
                    Fields.append(Field_circle)
        if typ2 == 'rectangle':
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
                    Fields.append(Field_rectangle)
        if typ2 == 'triangle':
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
                    Fields.append(Field_triangle)
        if typ2 == 'rhombus':
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
                    Fields.append(Field_rhombus)
        if typ2 != 'circle' and typ2 != 'rectangle' and typ2 != 'triangle' and typ2 != 'rhombus':
            print("Please give another type of figure")
            Names.remove(typ2)

    print(Names)
    print(Fields)

    if Fields[0]>Fields[1]:
        print("First field (",Names[0],") is bigger ")
    if Fields[0]<Fields[1]:
        print("Second field (",Names[1],") is bigger ")

compare_fields()