def squareper(x):
    perimeter=4*x
    print("perimeter of square is",perimeter)

def rectangleper(l,b):
    perimeter = 2*(l+b)
    return perimeter

def circumference(r):
    c = 2*3.14*r
    print("circumference of circle is")

r = int(input("enter radius of circle:"))
circumference(r)

x = int(input("enter side of square->"))
squareper(x)

l = int(input("enter the length of rectanglr->"))
b = int(input("enter the breadth of rectanglr->"))
print(rectangleper(l,b))