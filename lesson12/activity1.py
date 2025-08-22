r = float(input("enter radius:"))

def circle_circumference(r):
    return 2*3.14*r

print(circle_circumference(9))

def weather_condition():
    print("weather is peasent in",spring)
    print("weather is same in",autumn)

spring = "autumn"
autumn = "wimter"
weather_condition()

def add(p,q):
    return p+q

def subtract(p,q):
    return p-q

def multiply(p,q):
    return p*q

def divide(p,q):
    return p/q

print("please select opration.")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")

choice = input("please enter choice (a/b/c/d):")

num_1 = int(input("please enter first number:"))
num_2 = int(input("please enter second number:"))

if choice == 'a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice == 'b':
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))
elif choice == 'c':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice == 'd':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
    print("this is an invalid input")