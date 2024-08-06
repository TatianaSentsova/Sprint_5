import random


class Generations:
    # Генерирую пароль согласно требованиям:
    # Для регистрации используй почту в формате: имя_фамилия_номер когорты_любые 3 цифры@домен.
    # Например, testtestov1999@yandex.ru.
    # Это нужно, чтобы зарегистрироваться с уникальной почтой.
    @staticmethod
    def generate_login():
        domain = ['yandex.ru', 'gmail.com', 'mail.ru']
        return f'tatianasentsova9{random.randint(100, 999)}@{random.choice(domain)}'

    @staticmethod
    def generate_password():
        alphabet = [chr(i) for i in range(97, 123)]
        one_number = random.randint(0, 9)
        symbol = ['!', '@', '#', '+', '-', '.', '/', '<', '=', '>']
        three_number = random.randint(000, 999)
        return f'{one_number}{random.choice(alphabet)}{three_number}{random.choice(symbol)}'
