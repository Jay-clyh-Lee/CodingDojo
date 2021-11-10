class MathDojo:

    def __init__(self) -> None:
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for number in list(nums):
            self.result += number
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for number in list(nums):
            self.result -= number
        return self

math1 = MathDojo.add(1,2,3)