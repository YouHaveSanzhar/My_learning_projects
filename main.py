def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Введите номер операции (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Неверный выбор операции. Попробуйте снова.")
        return

    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")

    if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
        print("Ошибка: введите числовые значения.")
        return

    num1 = float(num1)
    num2 = float(num2)

    if choice == '1':
        print(f"Результат: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Результат: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Результат: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Ошибка: деление на ноль невозможно!")
        else:
            print(f"Результат: {num1} / {num2} = {num1 / num2}")


# Запуск калькулятора
calculator()
