class myClass:
    __privateVar = 27;

    def __privMteh(self):
        print("i am inside class myclass")

    def hello(self):
        print("Private variable value :",myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privMteh