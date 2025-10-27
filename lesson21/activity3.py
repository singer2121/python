import array as anglo

array_num = anglo.array('i', [1, 3,5,3,7,3,9,3,2,9,8,7,3,])
print("original array:" +str(array_num))
print("number of occuurrences of the number3 in the said array:"+str(array_num.count(3)))

array_num.reverse()
print("reverse the order of the items:")
print(str(array_num))