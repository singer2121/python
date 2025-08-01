medical_cause=input("did you have a medical cause Y or N:")
#take input of the attendence
atten = int(input("enter the attendence of the students: "))


if medical_cause == 'Y': #checking the condition 1
    print("you are allowed")
else:
    if atten>=75: #checking the condition 2
         print("allowed")
    else:
         print("not allowed")     