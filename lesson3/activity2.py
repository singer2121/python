#Assigning Different Variables
name = "Akshita"
age = 12
is_student = True
weight = 38.5

#printing different variables and their data type
print("name :",name)
print("data type of name is",type(name))

print("age :", age)
print("data type of age is", type(age))

print("is_student :", is_student)
print("data type of is_student is", type(is_student))

print("weight :", weight)
print("data type of weight is", type(weight))

#Type casting to convert the datatype of variables

print("\n After type casting.......")
age = str(age)
print(age)
print("Data type of age is", type(age))
weight=int(weight)
print(weight)
print("Data type of weight is", type(weight))