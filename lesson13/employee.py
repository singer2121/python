def worker(name):
    print(name)

def salary(exp):
    if exp>=5:
        return 3000000
    elif exp>=3:
         return 10000000
    else:
         return 21000000
    
worker("Akshita")
a = salary(21)
print("the salary of woker is",a)