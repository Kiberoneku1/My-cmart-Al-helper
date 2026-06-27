import itertools
import string
# Пароль, который взламываем
secret_password = "429gkdkh@2"
# Набор символов: цифры
charset = string.digits
def brute_force(charset, max_lenght):
    for lenght in range(1, max_lenght+1):
        for attempt in itertools.product(charset, repeat=lenght):
            attempt = "".join(attempt)
            print('Пробуем: ', attempt)
            if attempt == secret_password:
                return attempt

found = brute_force(charset, 10)
print("\nПароль найден:", found)