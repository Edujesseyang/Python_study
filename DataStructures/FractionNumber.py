import math


class FractionNum:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        other = FractionNum.to_fraction(other)

        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        gcd = math.gcd(new_numerator, new_denominator)
        return FractionNum(new_numerator // gcd, new_denominator // gcd)

    def substra(self, other):
        other = FractionNum.to_fraction(other)

        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        gcd = math.gcd(new_numerator, new_denominator)
        return FractionNum(new_numerator // gcd, new_denominator // gcd)

    def multiple(self, other):
        other = FractionNum.to_fraction(other)

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        gcd = math.gcd(new_numerator, new_denominator)
        return FractionNum(new_numerator // gcd, new_denominator // gcd)

    def divide(self, other):
        if other == 0:
            raise ZeroDivisionError("Cannot divide zero")
        other = FractionNum.to_fraction(other)

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        gcd = math.gcd(new_numerator, new_denominator)
        return FractionNum(new_numerator // gcd, new_denominator // gcd)

    def simplify(self):
        greatest_factor = math.gcd(self.denominator, self.numerator)  # Math.gcd() 为python自带取n数的最大公约数
        self.numerator = self.numerator // greatest_factor  # // 为整除操作
        self.denominator = self.denominator // greatest_factor

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    @staticmethod
    def to_fraction(num):
        denominator = 1
        if isinstance(num, FractionNum):
            return num
        elif isinstance(num, int):
            denominator = 1
        elif isinstance(num, float):
            s = str(num)
            if '.' in s:
                after_decimal = len(s.split('.')[1])
                num = int(num * (10 ** after_decimal))
                denominator = 10 ** after_decimal
        return FractionNum(num, denominator)


# test constructing
f1 = FractionNum(1, 3)
f2 = FractionNum(4, 7)

# test methods
print(f1.add(f2))
print(f1.substra(f2))
print(f1.multiple(f2))
print(f1.divide(f2))

# test chaining operations
print(f1.add(3).multiple(5).substra(12))
print(f1.add(3).multiple(5).substra(12).divide(f2))

# test catch errors
try:
    print(f1.add(3).multiple(5).substra(12).divide(0))
except ZeroDivisionError:
    print("Cannot divide zero")

try:
    f3 = FractionNum(1, 0)
except ValueError:
    print("Zero Denominator Error")
