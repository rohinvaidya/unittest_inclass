class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        if a is not None and b is not None:
            return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    