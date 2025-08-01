height = float(input("enter your height in cm:"))
weight = float(input("enter your weight in kg:"))

BMI = weight / (height/100)**2

print("your BMI is", BMI)

if BMI <= 18.4:
    print("you are underweight")

if BMI <= 24.9:
    print("you are healthy")

if BMI <= 29.9:
    print("you are overweight")

if BMI <= 34.9:
    print("you are severely over weight")

if BMI <= 39.9:
    print("you are obese")