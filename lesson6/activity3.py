print("select your ride")
print("1. bike")
print("2. car")

choice = int( input("enter your choice:"))

if( choice == 1): 
   print("what type of bike you want")
   print("1.scooty\n")
   print("2.scooter\n")

   choice2=int(input("enter you choice2 :"))
   if choice2==1:
        print("you have choosen scooty")
   else:
        print("you have choosen scooter")

elif( choice == 2 ):
   print("what type of car you want")
   print("1.SUV")
   print("2.Curv")
   choice3=int(input("enter you choice3 :"))
   if choice3==1:
    print("you have choosen SUV")
   else:
    print("you have choosen Curv")

else:
   print("wrong choice")