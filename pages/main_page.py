from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    @allure.step('Ждем отображения кнопки "Заказать" в шапке страницы')
    def wait_visibility_of_header_order_button(self):
        self.wait_visibility_of_element(OrderPageLocators.header_order_button)

    @allure.step('Нажимаем на кнопку "Заказать" в шапке страницы')
    def click_on_header_order_button(self):
        self.click_on_element(OrderPageLocators.header_order_button)

    @allure.step('Ждем отображения лого "Самокат" в шапке страницы')
    def wait_visibility_of_scooter_logo(self):
        self.wait_visibility_of_element(BasePageLocators.scooter_logo)

    @allure.step('Ждем отображения лого "Яндекс" в шапке страницы')
    def wait_visibility_of_yandex_logo(self):
        self.wait_visibility_of_element(BasePageLocators.yandex_logo)

    @allure.step('Нажимаем на лого "Самокат" в шапке страницы')
    def click_on_scooter_logo(self):
        self.click_on_element(BasePageLocators.scooter_logo)

    @allure.step('Нажимаем на лого "Яндекс" в шапке страницы')
    def click_on_yandex_logo(self):
        self.click_on_element(BasePageLocators.yandex_logo)

    @allure.step('Ждем загрузки заголовка "Самокат на пару дней" на главной')
    def wait_visibility_of_scooter_header(self):
        self.wait_visibility_of_element(BasePageLocators.scooter_header)

    @allure.step('Проверяем отображение заголовка "Самокат на пару дней" на главной')
    def check_displaying_of_scooter_header(self):
        return self.check_displaying_of_element(BasePageLocators.scooter_header)

    @allure.step('Скроллим страницу до раздела "Вопросы о важном" и кликаем по вопросу')
    def scroll_and_check_questions_answers_section(self, data):
        self.scroll_to_element(MainPageLocators.questions_answers_section)
        self.wait_visibility_of_element(MainPageLocators.questions[data])
        self.click_on_element(MainPageLocators.questions[data])
        self.check_displaying_of_element(MainPageLocators.answers[data])

    @allure.step('Ждем отображения ответа после клика по вопросу в разделе "Вопросы о важнoм"')
    def wait_visibility_of_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.answers[data])

    @allure.step('Получаем текст ответа в разделе "Вопросы о важнoм"')
    def get_text_of_answer(self, data):
        return self.get_text_of_element(MainPageLocators.answers[data])
