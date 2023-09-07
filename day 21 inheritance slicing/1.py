class Animal():
    def __init__(self):
        self.num_of_eyes = 2
        self.legs = 4

    def breath(self):
        print("Inhale , Exahle")

    # def legs(self):




class Fish (Animal):
    def __int__(self):
        super().__init__()

    def swim(self):
        print("I can swim")

    def breath(self):
        super().breath()
        print("Under Water")

mimi = Fish()
print(mimi.num_of_eyes)
mimi.breath()
mimi.swim()
print(mimi.legs)     