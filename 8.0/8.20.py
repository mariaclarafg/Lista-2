class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def show_data(self):
        print(f"{self.numerator}/{self.denominator}")

    def multiply(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
print("Fraction 1:")
fraction1.show_data()

print("Multiplication result:")
result = fraction1.multiply(fraction2)
result.show_data()
