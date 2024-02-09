'''Testing My Calculator'''
class Calculator
def __init__(self):
    self.history = []

    def add (self, a, b):
        result = a + b 
        self.history.append((f"[a] + [b]", result))
        return result
    
     def subtract (self, a, b):
        result = a - b 
        self.history.append((f"[a] - [b]", result))
        return result
    
     def multiply (self, a, b):
        result = a * b 
        self.history.append((f"[a] * [b]", result))
        return result
    
    def divide (self, a, b):
        if b == 0:
            return "Error: Cannot divide by 0."
        result = a / b 
        self.history.append((f"[a] / [b]", result))
        return result
    
    def get_history(self):
        return self.history
    
    def menu():
        calculator = Calculator()
        while True:
            print
