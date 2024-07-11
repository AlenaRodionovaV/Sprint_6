from pages.main_page import MainPage
from conftest import driver
import allure


class TestLogosClick:

    @allure.title('Проверка перехода на главную при клике на лого "Самокат" в шапке страницы')
    def test_going_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_order_button()
        main_page.click_on_header_order_button()
        main_page.wait_visibility_of_scooter_logo()
        main_page.click_on_scooter_logo()
        main_page.wait_visibility_of_scooter_header()
        assert main_page.check_displaying_of_scooter_header()

    @allure.title('Проверка перехода на страницу "Дзен" при клике на лого "Яндекс"')
    def test_going_to_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_yandex_logo()
        main_page.click_on_yandex_logo()
        main_page.switch_to_next_tab()
        assert main_page.check_visibility_of_logo() == 'Дзен'
