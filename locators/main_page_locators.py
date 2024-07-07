from selenium.webdriver.common.by import By


class MainPageLocators:

    questions_answers_section = By.XPATH, '//div[contains(@class, "Home_FAQ")]' # заголовок раздела "Впоросы о важном"

    questions = {
        1: [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'], # вопрос "Сколько это стоит? И как оплатить?"
        2: [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'], # вопрос "Хочу сразу несколько самокатов. Так можно?"
        3: [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'], # вопрос "Как рассчитывается время аренды?"
        4: [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'], # вопрос "Можно ли заказать самокат прямо на сегодня?"
        5: [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'], # вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
        6: [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'], # вопрос "Вы привозите зарядку вместе с самокатом?"
        7: [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'], # вопрос "Можно ли отменить заказ?"
        8: [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div'] # вопрос "Я живу за МКАДом, привезете?"
    }

    answers = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'), # ответ на "Сколько это стоит? И как оплатить?"
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'), # ответ на "Хочу сразу несколько самокатов. Так можно?"
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'), # ответ на "Как рассчитывается время аренды?"
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'), # ответ на "Можно ли заказать самокат прямо на сегодня?"
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'), # ответ на "Можно ли продлить заказ или вернуть самокат раньше?"
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'), # ответ на "Вы привозите зарядку вместе с самокатом?"
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'), # ответ на "Можно ли отменить заказ?"
        8: (By.XPATH, '//div[@id="accordion__panel-7"]') # ответ на "Я живу за МКАДом, привезете?"
    }
