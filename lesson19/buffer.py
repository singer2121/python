fruits = ("apple","cherry","mango")
print("Fruits tuple:",fruits)

print("First Fruits:",fruits[0])
print("Second Fruits:",fruits[1])

print("All fruits:")
for fruit in fruits:
    print(fruit)

if "cherry" in fruits:
    print("Yes,cherry is in the tuple.")

print("Totla fruits:",len(fruits))

more_fruits=("orange","grapes")
all_fruits = fruits+more_fruits
print("All fruits combined",all_fruits)