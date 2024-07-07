from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def wait_visibility_of_header_order_button(self):
        self.wait_visibility_of_element(OrderPageLocators.header_order_button)

    def click_on_header_order_button(self):
        self.click_on_element(OrderPageLocators.header_order_button)

    def wait_visibility_of_scooter_logo(self):
        self.wait_visibility_of_element(BasePageLocators.scooter_logo)

    def wait_visibility_of_yandex_logo(self):
        self.wait_visibility_of_element(BasePageLocators.yandex_logo)

    def click_on_scooter_logo(self):
        self.click_on_element(BasePageLocators.scooter_logo)

    def click_on_yandex_logo(self):
        self.click_on_element(BasePageLocators.yandex_logo)

    def wait_visibility_of_scooter_header(self):
        self.wait_visibility_of_element(BasePageLocators.scooter_header)

    def check_displaying_of_scooter_header(self):
        return self.check_displaying_of_element(BasePageLocators.scooter_header)

    def scroll_and_check_questions_answers_section(self, data):
        self.scroll_to_element(MainPageLocators.questions_answers_section)
        self.wait_visibility_of_element(MainPageLocators.questions[data])
        self.click_on_element(MainPageLocators.questions[data])
        self.check_displaying_of_element(MainPageLocators.answers[data])

    def wait_visibility_of_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.answers[data])

    def get_text_of_answer(self, data):
        return self.get_text_of_element(MainPageLocators.answers[data])
