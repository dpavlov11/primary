import random


def start_game():
    print("ИГРА 'УГАДАЙ ЧИСЛО' ")
    print("Инструкция: Компьютер загадал число. Ваша задача — угадать его за ограниченное число попыток.")

    # Настройки (Адаптивность)
    low, high = 1, 100
    max_attempts = 10
    secret_number = random.randint(low, high)
    attempts_left = max_attempts

    print(f"Я загадал число от {low} до {high}. У вас есть {max_attempts} попыток.")

    while attempts_left > 0:
        print(f"\nОсталось попыток: {attempts_left}")
        user_input = input("Введите ваше число (или 'exit' для выхода): ").strip().lower()

        if user_input == 'exit':
            print("Игра завершена.")
            break

        # Валидация ввода
        try:
            guess = int(user_input)
            if not (low <= guess <= high):
                print(f"Пожалуйста, введите число именно в диапазоне от {low} до {high}.")
                continue
        except ValueError:
            print("Ошибка: введите целое число.")
            continue

        attempts_left -= 1

        # Проверка и обратная связь
        if guess == secret_number:
            print(f"🎉 ПОЗДРАВЛЯЮ! Вы угадали число {secret_number}!")
            break
        elif guess < secret_number:
            print("Слишком маленькое.")
        else:
            print("Слишком большое.")

        # Подсказка (Игровая логика)
        if attempts_left == 3:
            print(
                f"--- ПОДСКАЗКА: Число находится в диапазоне от {max(low, secret_number - 10)} до {min(high, secret_number + 10)} ---")

    if attempts_left == 0 and guess != secret_number:
        print(f"\nВы проиграли! Максимальное количество попыток исчерпано. Было загадано: {secret_number}")

    # Повторная игра
    play_again = input("\nХотите сыграть еще раз? (y/n): ").lower()
    if play_again == 'y':
        start_game()
    else:
        print("Спасибо за игру! До свидания.")


if __name__ == "__main__":
    start_game()
