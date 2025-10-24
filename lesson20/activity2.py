test_dict = {'Akshita': 2, 'likes':2, 'color':2, 'lavender':12}

print("the orignal dictionary:" + str(test_dict))

K = 2

res = 0 
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1 

print("Frequency of K is :"+ str(res))