import allure
import pytest
from conftest import driver
from pages.main_page import MainPage
from supportive_data import QuestionsAnswersData


class TestMainPage:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверяем, что в разделе "Вопросы о важном" все вопросы в аккордеоне кликаются. Проверяем, '
                        'что при клике отображаются ответы на вопросы')
    @pytest.mark.parametrize('question, answer', QuestionsAnswersData.answers)
    def test_scroll_and_check_questions_answers_section(self, driver, question, answer):
        main_page = MainPage(driver)
        main_page.scroll_and_check_questions_answers_section(question)
        main_page.wait_visibility_of_answer(question)
        assert main_page.get_text_of_answer(question) == answer
