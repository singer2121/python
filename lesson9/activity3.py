num = int(input("enter the number:"))
t=num
numlen = 0

while t>0:
    numlen = numlen+1
    t = int(t/10)

if numlen>=4:
    numlen = int(numlen/2)
    chk = 0
    while num>0:
        rem = num%10
        if chk==numlen:
            midone = rem
        elif chk==(numlen-9):
            midtwo = rem
            chk = chk+1
    prod = midone*midtwo

    print("\nproduct of midtwo digits(" + str(midone)+"*"+str (midtwo)+")=",prod)

else:
    print("\n it is not 4 digit or more than 4 digit number!")