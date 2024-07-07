from selenium.webdriver.common.by import By


class BasePageLocators:

    scooter_header = By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]' # текст "Самокат на пару дней" на главной
    scooter_logo = By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]' # кликабельный логотип "Самокат" в шапке на главной
    yandex_logo = By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]' # кликабельный логотип "Яндекс" в шапке на главной
    dzen_logo = By.TAG_NAME, 'title' # кликабельный логотип "Дзен" на странице Дзена
