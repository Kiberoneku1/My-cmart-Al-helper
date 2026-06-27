import random
import string


def generate_password():
    """
    Простой генератор паролей с меню выбора
    """
    print("=" * 40)
    print("         ГЕНЕРАТОР ПАРОЛЕЙ")
    print("=" * 40)

    # Запрашиваем длину пароля
    while True:
        try:
            length = int(input("Введите длину пароля (минимум 4): "))
            if length < 4:
                print("Длина пароля должна быть не менее 4 символов!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число!")

    # Меню выбора сложности
    print("\nВыберите сложность пароля:")
    print("1 - Только цифры")
    print("2 - Цифры + буквы (нижний регистр)")
    print("3 - Цифры + буквы (верхний и нижний регистр)")
    print("4 - Цифры + буквы + специальные символы")

    while True:
        try:
            choice = int(input("Ваш выбор (1-4): "))
            if choice < 1 or choice > 4:
                print("Пожалуйста, выберите 1, 2, 3 или 4!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число!")

    # Формируем набор символов в зависимости от выбора
    if choice == 1:
        chars = string.digits
        description = "только цифры"
    elif choice == 2:
        chars = string.digits + string.ascii_lowercase
        description = "цифры + строчные буквы"
    elif choice == 3:
        chars = string.digits + string.ascii_letters
        description = "цифры + буквы (оба регистра)"
    else:  # choice == 4
        chars = string.digits + string.ascii_letters + string.punctuation
        description = "цифры + буквы + спецсимволы"

    # Генерируем пароль
    password = ''.join(random.choice(chars) for _ in range(length))

    # Выводим результат
    print("\n" + "=" * 40)
    print("Сгенерированный пароль:")
    print(f"Сложность: {description}")
    print(f"Длина: {length} символов")
    print("-" * 40)
    print(f"Пароль: {password}")
    print("=" * 40)

    return password


# Запуск генератора
if __name__ == "__main__":
    generate_password()

    # Спрашиваем, хочет ли пользователь сгенерировать еще один пароль
    while True:
        again = input("\nХотите сгенерировать еще один пароль? (д/н): ").lower()
        if again in ['д', 'да', 'y', 'yes']:
            print("\n" * 2)  # Добавляем отступы
            generate_password()
        else:
            print("Спасибо за использование генератора паролей!")
            break