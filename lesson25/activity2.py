class student:

    def _init_(self):
        print('Student created')

    def _del_(self):
        print("Destructor called")

def create_obj():
    print('making object.....')
    obj = student
    print('function end......')
    return obj

print('calling create_obj() function.......')
obj = create_obj()
print('program end ..........')