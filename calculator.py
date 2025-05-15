print("Running Calculator...")

class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(a, b):
        try:
            return a / b  # Using float division
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."


def get_numbers(count=2, multi=False):
    while True:
        try:
            if multi:
                nums = input("Enter numbers separated by space: ")
                num_list = list(map(float, nums.strip().split()))
                if len(num_list) < 2:
                    print("Please enter at least two numbers.")
                    continue
                return num_list
            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                return a, b
        except ValueError:
            print("Invalid input. Please enter only numbers.")


while True:
    try:
        op = input("\nEnter operator (+, -, *, /) or 'q' to quit: ").strip()

        if op.lower() == 'q':
            print("Calculator exited.")
            break

        if op == '+':
            nums = get_numbers(multi=True)
            print("Result:", Calculator.add(*nums))

        elif op == '*':
            nums = get_numbers(multi=True)
            print("Result:", Calculator.multiply(*nums))

        elif op == '-':
            a, b = get_numbers()
            print("Result:", Calculator.subtract(a, b))

        elif op == '/':
            a, b = get_numbers()
            print("Result:", Calculator.divide(a, b))

        else:
            print("Invalid operator. Please choose from +, -, *, / or 'q'.")

    except Exception as e:
        print(f"Unexpected error occurred: {e}")
