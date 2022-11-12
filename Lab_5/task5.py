import random
import string


def get_random_password() -> str:
    n = 8  # нужно 8 символов
    passw = random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, n)
    # TODO написать функцию генерации случайных паролей
    password = "".join(passw)  # убираем соединительные символы
    return password


print(get_random_password())
