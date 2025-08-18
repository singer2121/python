n = int(input("enter number of rows:"))

m =int(input("enter number of colums:"))
for i in range(1,n,2):
    print((i * ".|.").center(m, "-"))
print("AKSHITA".center(m,"-"))
for i in range(n-2,-1,-2):
    print((i *".|.".center(m, "-")))   