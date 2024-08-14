from generations import Generations


class TestData:
    NAME = 'Таня'
    EMAIL = Generations.generate_login()
    PASSWORD = Generations.generate_password()
    INVALID_PASSWORD = Generations.generate_password()[0:5]
    USER_EMAIL = 'tatianasentsova9000@yandex.ru'
    USER_PASSWORD = '1a456$'


class ApplicationData:
    STELLAR_BURGERS_URL = 'https://stellarburgers.nomoreparties.site/'
