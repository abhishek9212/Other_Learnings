class Calculator:

    def __init__(self, num):
        self.number = num

    @staticmethod
    def greet():
        print("*********Hello User! Welcome to World's best Calculator!!!*********")

    def square(self):
        print(f"The square of {self.number} is: {self.number ** 2} ")

    def squareRoot(self):
        print(f"The square root of {self.number} is: {self.number ** 0.5} ")

    def cube(self):
        print(f"The cube of {self.number} is: {self.number ** 3} ")

a = Calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()
