class Calculator:

    @staticmethod
    def convert_operation(operation):
        match operation:
            case 1:
                return "+"
            case 2:
                return "-"
            case 3:
                return "*"
            case 4:
                return "/"

    @staticmethod
    def sum(x, y):
        return x + y
    
    @staticmethod
    def difference(x, y):
        return x - y
    
    @staticmethod
    def product(x, y):
        return x * y

    @staticmethod
    def quotient(x, y):
        if y == 0:
            raise ZeroDivisionError("Nie dzielimy przez 0")
        return x / y
    
if __name__ == "__main__":
    print("- Dodawanie: 1")
    print("- Odejmowanie: 2")
    print("- Mnozenie: 3")
    print("- Dzielenie: 4")
    operation = Calculator.convert_operation(float(input("Wybierz numer operacji: ")))

    number1 = float(input("Podaj pierwszą liczbe: "))
    number2 = float(input("Podaj druga liczbe: "))

    if operation == "+":
        print("WYNIK: ")
        print(number1, operation, number2, "=", Calculator.sum(number1, number2))
    elif operation == "-":
        print("WYNIK: ")
        print(number1, operation, number2, "=", Calculator.difference(number1, number2))
    elif operation == "*":
        print("WYNIK: ")
        print(number1, operation, number2, "=", Calculator.product(number1, number2))
    elif operation == "/":
        print("WYNIK: ")
        print(number1, operation, number2, "=", Calculator.quotient(number1, number2))
    else:
        print("Zly wybor operacji")

