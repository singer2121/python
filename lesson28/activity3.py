class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely sponken lanuage of India.")

    def type(self):
        print("India is an developing country.")

class USA():
    def capital(self):
        print("Washington D.C. is the capital of USA.")

    def language(self):
        print("English is the most widely sponken lanuage of USA.")

    def type(self):
        print("USA is an developed country.")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind,obj_usa):
    country. capital()
    country.language()
    country.type()