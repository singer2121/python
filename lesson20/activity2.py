test_dict = {'Akshita': 21, 'likes':21, 'color':2, 'pastel blue':2}

print("the orignal dictionary:" + str(test_dict))

K = 21

res = 0 
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1 

print("Frequency of K is :"+ str(res))