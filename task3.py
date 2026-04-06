import math as m

def calculate(choice, x, y):
    if choice == "add":
        return x + y
    elif choice == "sub":
        return x - y
    elif choice == "mul":
        return x * y
    elif choice == "div":
        if y == 0:
            return "Помилка: ділення на нуль"
        return x / y
    elif choice == "pow":
        return x ** y
    elif choice == "sqrt":
        return (m.sqrt(x), m.sqrt(y))
    else:
        return None


operation = input("Виберіть дію (add, sub, mul, div, pow, sqrt): ").lower().strip()

if operation:
    try:
        a = float(input("Перше число: "))
        b = float(input("Друге число: "))

        answer = calculate(operation, a, b)

        if answer is None:
            print("Невідома операція!")
        else:
            print("Відповідь:", answer)

    except:
        print("Сталася помилка при введенні!")
else:
    print("Операцію не введено!")