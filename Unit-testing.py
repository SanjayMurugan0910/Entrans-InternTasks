import unittest
class TestingCalculator(unittest.TestCase):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero") 
        else:
            return a / b
valid_calculator = TestingCalculator()
assert valid_calculator.add(5, 3) == 8
assert valid_calculator.subtract(10, 4) == 6    
assert valid_calculator.multiply(7, 6) == 42
assert valid_calculator.divide(20, 5) == 4

try:
    valid_calculator.divide(10, 0)
except ValueError as e:
    assert str(e) == "Cannot divide by zero"
    print("All tests passed!")
    
    
if __name__ == '__main__':  
    unittest.main()
