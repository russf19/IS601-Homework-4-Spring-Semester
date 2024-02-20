from decimal import Decimal
from calculator.calculation import Calculation
from calculator.history import History

class Operation:
    @staticmethod
    def perform_operation(operation: str, a: float, b: float) -> float:
        operations = {
            'add': Calculation.add,
            'subtract': Calculation.subtract,
            'multiply': Calculation.multiply,
            'divide': Calculation.divide
        }
        
        if operation not in operations:
            raise ValueError("Invalid operation.")
        
        result = operations[operation](a, b)
        History.add_history(operation, result)
        return result

    @staticmethod
    def get_last_calculation() -> str:
        operation, result = History.get_history()
        return f"Last {operation}: {result}"