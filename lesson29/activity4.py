import random

class FruitQuiz:

    def __init__(self):

        self.fruits={'cherry':'red',
                     'Mango':'yellow',
                     'Watermelon':'green',
                     'Blueberry':'blue'}
        

def quiz(self):
    while(True):

        fruit, color = random.choice(list(self.fruit.item()))

        print("what is color of{}".format(fruit))
        user_answer = input()

        if(user_answer.lower()== color):
            print("Correct answer")
        else:
            print("Wrong answer")

        option = int(input("enter 0 , if you want to play again otherwise enter 1 :"))
        if(option):
            break


print("Welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()