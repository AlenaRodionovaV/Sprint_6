from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_visibility_of_logo(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(
            BasePageLocators.dzen_logo))
        return self.driver.title

    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()
