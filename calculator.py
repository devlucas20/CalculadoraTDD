# calculator.py

class Calculator:
    def add(self, a, b):
        """Retorna a soma de a e b."""
        return a + b

    def subtract(self, a, b):
        """Retorna a subtração de b de a."""
        return a - b

    def multiply(self, a, b):
        """Retorna o produto de a e b."""
        return a * b

    def divide(self, a, b):
        """Retorna a divisão de a por b. Levanta ZeroDivisionError se b for zero."""
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        return a / b
