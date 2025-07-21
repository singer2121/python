# Taking total amount as input from user
Amount =int(input("please enter the amount for withdraw :"))

#Calculating the number of notes of different denominations
note_1= Amount//100
note_2= (Amount%100)//50
note_3= ((Amount%100)%50)//10

print("notes of 100 rupree",note_1)
print("notes of 50 rupree",note_2)
print("notes of 10 rupree",note_3)