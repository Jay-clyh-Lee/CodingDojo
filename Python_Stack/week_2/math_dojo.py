class MathDojo:

    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            self.result -= num
        return self

    def display(self):
        print(self.result)

math1 = MathDojo()
math1.add(1,2,3,213,32131,44123).subtract(1,231,321,21,3).display()

