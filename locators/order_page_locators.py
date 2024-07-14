from selenium.webdriver.common.by import By


class OrderPageLocators:

    main_order_button = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button' # кнопка 'Заказать' на главной странице после блока "Как это работает"
    header_order_button = By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]' # кнопка 'Заказать' в шапке страницы

    order_scooter_text = (By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]") # текст "Для кого самокат" на странице заказа
    name_input = (By.XPATH, "//input[@placeholder='* Имя']") # поле для ввода имени
    surname_input = (By.XPATH, "//input[@placeholder='* Фамилия']") # поле для ввода фамилии
    address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # поле для ввода адреса
    metro_input = (By.XPATH, "//input[@placeholder='* Станция метро']") # поле для выбора станции метро
    metro_dropdown = (By.XPATH, ".//li[@class='select-search__row']") # селект со станциями метро
    phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # поле для ввода номера телефона
    next_button = (By.XPATH, "//button[text()='Далее']") # кнопка 'Далее' под формой заполнения данных

    about_rent_text = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]") # текст "Про аренду" на странице заказа
    date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # поле для ввода даты доставки самоката
    datepicker = (By.XPATH, "//div[@class='react-datepicker-popper']") # выпадающий календарь
    datepicker_item = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]") # число в календаре
    rent_select = (By.XPATH, ".//div[text()='* Срок аренды']") # поле для выбора срока аренды
    rent_dropdown = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']") # селект с вариантами срока аренды
    colour_checkbox = (By.XPATH, "//input[@id='grey']") # чек-бокс для выбора цвета самоката
    comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # поле для ввода комментария для курьера
    make_order_button = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']") # кнопка 'Заказать' под формой заполнения условий аренды

    confirm_order_button = (By.XPATH, "//button[text()='Да']") # кнопка 'Да' на модалке "Хотите оформить заказ?"
    check_status_button = (By.XPATH, ".//*[text()='Посмотреть статус']") # кнопка 'Посмотреть статус' на модалке "Заказ оформлен"
