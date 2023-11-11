import random



num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
class EncapsulatedMathOperation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def perform_random_operation(self):
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            result = self.num1 + self.num2
        elif operation == '-':
            result = self.num1 - self.num2
        elif operation == '*':
            result = self.num1 * self.num2
        elif operation == '/':
            # Избегаем деления на ноль
            if self.num2 != 0:
                result = self.num1 / self.num2
            else:
                result = "Деление на ноль -"

        return result




math_operation = EncapsulatedMathOperation(num1, num2)
result = math_operation.perform_random_operation()


print(f"Результат вычислений: {result}")