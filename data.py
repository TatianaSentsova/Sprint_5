from generations import Generations


class Data:
    STELLAR_BURGERS_URL = 'https://stellarburgers.nomoreparties.site/'
    NAME = 'Таня'
    EMAIL = Generations.generate_login()
    PASSWORD = Generations.generate_password()
    INVALID_PASSWORD = Generations.generate_password()[0:5]
    USER_EMAIL = 'tatianasentsova9000@yandex.ru'
    USER_PASSWORD = '1a456$'
