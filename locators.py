from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    # кнопка "Войти в аккаунт" на главной странице
    SIGN_IN_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")

    # ссылка на форму регистрации
    SIGN_UP_LINK = (By.XPATH, ".//a[(@class = 'Auth_link__1fOlj') and (text() = 'Зарегистрироваться')]")

    # поле для ввода имени
    USER_NAME_FIELD = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")

    # поле для ввода email
    USER_EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")

    # поле для ввода пароля
    USER_PASSWORD_FIELD = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")

    # кнопка "Зарегестрироваться"
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")

    # кнопка входа в аккаунт
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")

    # кнока "Оформить заказ"
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")

    # кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href = '/account']")

    # сообщение об ошибке при регистрации с неккоректным паролем
    INVALID_PASSWORD_MESSAGE = (By.XPATH, ".//p[@class = 'input__error text_type_main-default']")

    # ссылка "Войти"
    SIGN_IN_LINK = (By.XPATH, ".//a[(@class = 'Auth_link__1fOlj') and (text() = 'Войти')]")

    # ссылка "Восстановить пароль"
    RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[@href = '/forgot-password']")

    # информация о пользователе
    PROFILE_INFORMATION = (By.XPATH, ".//a[(@href = '/account/profile') and (text() = 'Профиль')]")

    # кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")

    # заголовок соберите бургер
    MAKE_BURGER = (By.XPATH, ".//h1[text() = 'Соберите бургер']")

    # ссылка на логотип
    LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

    # кнопка "Выход" из аккаунта
    LOG_OUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")

    # вкладка "Булки" в активном и неактивном состоянии
    BUNS_ACTIVE = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text() = 'Булки']")
    BUNS_IN_ACTIVE = (By.XPATH, ".//div[contains(@class, '1SPyG  pt-4')]/span[text() = 'Булки']")

    # вкладка "Соусы" в активном и неактивном состоянии
    SAUCES_ACTIVE = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text() = 'Соусы']")
    SAUCES_IN_ACTIVE = (By.XPATH, ".//div[contains(@class, '1SPyG  pt-4')]/span[text() = 'Соусы']")

    # вкладка "Начинки" в активном и неактивном состоянии
    FILLINGS_ACTIVE = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text() = 'Начинки']")
    FILLINGS_IN_ACTIVE = (By.XPATH, ".//div[contains(@class, '1SPyG  pt-4')]/span[text() = 'Начинки']")

    # заголовки "Булки", "Соусы" и "Начинки" в меню ингридиентов
    SECTION_BUNS = (By.XPATH, ".//div[contains(@class, '__Xu3Mo')]/h2[text() = 'Булки']")
    SECTION_SAUCES = (By.XPATH, ".//div[contains(@class, '__Xu3Mo')]/h2[text() = 'Соусы']")
    SECTION_FILLINGS = (By.XPATH, ".//div[contains(@class, '__Xu3Mo')]/h2[text() = 'Начинки']")
