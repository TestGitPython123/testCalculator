print("Добро пожаловать в калькулятор")

first_value = float(input("Введите первое число: "))
second_value = float(input("Введите второе число: "))

operation = input("Введите символ операции: ")

if operation == "+":
    print(f"{first_value} + {second_value} "
          f"= {first_value + second_value}")
elif operation == "-":
    print(f"{first_value} - {second_value} "
          f"= {first_value - second_value}")
elif operation == "/":
    print(f"{first_value} / {second_value} "
          f"= {first_value / second_value}")
elif operation == "*":
    print(f"{first_value} * {second_value} "
          f"= {first_value / second_value}")