from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from supportive_data import UserData
import allure


class OrderPage(BasePage):

    @allure.step('Заполняем форму "Для кого самокат"')
    def enter_user_data_for_whom_scooter_form(self, test_data: object) -> object:
        self.wait_visibility_of_element(OrderPageLocators.name_input)
        self.click_on_element(OrderPageLocators.name_input)
        self.send_keys_to_input(OrderPageLocators.name_input, test_data[0])
        self.click_on_element(OrderPageLocators.surname_input)
        self.send_keys_to_input(OrderPageLocators.surname_input, test_data[1])
        self.click_on_element(OrderPageLocators.address_input)
        self.send_keys_to_input(OrderPageLocators.address_input, test_data[2])
        self.click_on_element(OrderPageLocators.metro_input)
        self.send_keys_to_input(OrderPageLocators.metro_input, test_data[3])
        self.click_on_element(OrderPageLocators.metro_dropdown)
        self.click_on_element(OrderPageLocators.phone_input)
        self.send_keys_to_input(OrderPageLocators.phone_input, test_data[4])
        self.click_on_element(OrderPageLocators.next_button)

    @allure.step('Заполняем форму "Про аренду"')
    def enter_data_for_rent_form(self, test_data: object):
        self.wait_visibility_of_element(OrderPageLocators.date_input)
        self.click_on_element(OrderPageLocators.date_input)
        self.send_keys_to_input(OrderPageLocators.date_input, test_data[5])
        self.click_on_element(OrderPageLocators.colour_checkbox)
        self.click_on_element(OrderPageLocators.rent_select)
        self.click_on_element(OrderPageLocators.rent_dropdown)
        self.click_on_element(OrderPageLocators.comment_input)
        self.send_keys_to_input(OrderPageLocators.comment_input, test_data[6])
        self.click_on_element(OrderPageLocators.make_order_button)
        self.wait_visibility_of_element(OrderPageLocators.confirm_order_button)
        self.click_on_element(OrderPageLocators.confirm_order_button)

    @allure.step('Выбираем станцию в выпадающем списке станций метро')
    def select_metro_station_in_rent_form(self):
        self.click_on_element(OrderPageLocators.metro_dropdown)

    @allure.step('Заполняем поле для ввода даты доставки самоката')
    def fill_date_input(self):
        (self.send_keys_to_input(*OrderPageLocators.date_input).send_keys(UserData.data_user_1[5]))

    @allure.step('Выбираем даату доставки самоката в выпадающем календаре')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.datepicker_item)

    @allure.step('Проверяем отображение кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.check_status_button)
