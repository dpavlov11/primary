import random

def guess_number_game():
    print("--- ИГРА: УГАДАЙ ЧИСЛО ---")
    print("Инструкция: Я загадал число от 1 до 100. У вас есть 10 попыток.")

    secret_number = random.randint(1, 100)
    attempts_left = 10

    while attempts_left > 0:
        try:
            print(f"\nОсталось попыток: {attempts_left}")
            user_input = input("Введите ваше число (или 'exit' для выхода): ")
            
            if user_input.lower() == 'exit':
                print("Игра прервана.")
                return

            guess = int(user_input)

            if not (1 <= guess <= 100):
                print("Ошибка: Число должно быть от 1 до 100.")
                continue

            attempts_left -= 1

            if guess == secret_number:
                print(f"Поздравляю! Вы угадали число {secret_number}!")
                return
            elif guess < secret_number:
                print("Слишком маленькое.")
            else:
                print("Слишком большое.")

            # Подсказка, когда осталось мало попыток
            if attempts_left == 3:
                low_hint = max(1, secret_number - 15)
                high_hint = min(100, secret_number + 15)
                print(f"--- ПОДСКАЗКА: Число находится в диапазоне от {low_hint} до {high_hint} ---")

        except ValueError:
            print("Ошибка: Введите целое число.")

    print(f"\nВы проиграли! Попытки закончились. Было загадано: {secret_number}")

if __name__ == "__main__":
    guess_number_game()
