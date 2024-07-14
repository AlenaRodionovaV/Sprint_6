from conftest import driver
import pytest
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from supportive_data import UserData
import allure

class TestOrderPage:

    @allure.title('Проверка оформления заказа')
    @allure.description('Проверяем, что заказ можно оформить двумя способами: нажатием кнопки "Заказать" на главной '
                        'странице, а также нажатием кнопки "Заказать" в шапке страницы')
    @pytest.mark.parametrize('input, test_data', [(OrderPageLocators.header_order_button, UserData.data_user_1),
                                                  (OrderPageLocators.main_order_button, UserData.data_user_2)])
    def test_successful_scooter_order_two_variants(self, driver, input, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(input)
        order_page.wait_visibility_of_element(input)
        order_page.click_on_element(input)
        order_page.enter_user_data_for_whom_scooter_form(test_data)
        order_page.enter_data_for_rent_form(test_data)
        assert order_page.check_displaying_of_button_check_status_of_order()
