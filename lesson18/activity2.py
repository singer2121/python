L = [4,5,1,2,9,7,10,8]
print("orignal list:",L)

sum = 0

for i in L:
    sum +=i

    avg = sum/len(L)
    print("sum =", sum)
    print("avg =", avg)

    L.sort()
    print ("smallest element is",L[0])

    print ("largest element is",L[-1])