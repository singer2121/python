# take marks as input from user
print("enter your marks you obtained in 6 subjects : ")
maths=int(input("maths :"))
sst=int(input("sst :"))
punjabi=int(input("punjabi :"))
science=int(input("science :"))
hindi=int(input("hindi :"))
english=int(input("english :"))

# ley's calculate the percentage of the marks
sum=maths+sst+punjabi+science+hindi+english
print("sum of maths,sst,punjabi,science,hindi,english")

perc = (sum/600)*100

print(end="percentage mark =")
print(perc)