import math
import sys


def get_factorial():
    # Увеличим лимит для очень больших чисел
    sys.set_int_max_str_digits(0)
    user_input = input("Введите положительное целое число: ")
    try:
        # Проверка на ввод нечисловых данных
        number = int(user_input)
        # Проверка на отрицательные числа
        if number < 0:
            print("Ошибка: Число должно быть положительным")
            return
        # библиотека math
        result = math.factorial(number)
        print(f"Факториал числа {number} успешно вычислен!")
        # При слишком длинном числе, выводим запрос отобразить только часть или подтверждаем
        if number > 1000:
            confirm = input("Результат очень большой. Вывести его полностью? (y/n): ")
            if confirm.lower() == 'y':
                print(result)
        else:
            print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: Введены некорректные данные. Пожалуйста, введите целое число.")
if __name__ == "__main__":
    get_factorial()
