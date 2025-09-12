import pytest
import allure
from main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import TestData


class TestMainPage:
    """Тесты главной страницы сервиса Самокат."""

    @allure.feature('FAQ раздел')
    @allure.story('Проверка ответов на вопросы в FAQ')
    @pytest.mark.parametrize(
        'question_number, expected_text',
        TestData.test_data_question_answer,
        ids=[
            'question_1_about_cost',
            'question_2_about_multiple_scooters',
            'question_3_about_today_order',
            'question_4_about_tomorrow_order',
            'question_5_about_extending_order',
            'question_6_about_charging',
            'question_7_about_cancellation',
            'question_8_about_delivery_radius'
        ]
    )
    def test_faq_question_contains_expected_text(
        self, driver, question_number, expected_text
    ):
        """Проверяет, что ответ на вопрос FAQ содержит ожидаемый текст."""
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        
        assert main_page.verify_faq_answer_contains_text(
            question_number, expected_text
        ), (f'Ответ на вопрос {question_number} не содержит '
            f'ожидаемый текст')

    @allure.feature('Навигация')
    @allure.story('Переход на страницу заказа через кнопку в хедере')
    def test_header_order_button_redirects_to_order_page(self, driver):
        """Проверяет переход на страницу заказа через кнопку в хедере."""
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        
        current_url = main_page.get_current_url()
        assert '/order' in current_url, (
            f'Ожидался переход на страницу заказа, текущий URL: {current_url}'
        )

    @allure.feature('Навигация')
    @allure.story('Переход на страницу заказа через кнопку в основном разделе')
    def test_main_order_button_redirects_to_order_page(self, driver):
        """Проверяет переход на страницу заказа через кнопку в основном разделе."""
        main_page = MainPage(driver)
        main_page.click_main_order_button()
        
        current_url = main_page.get_current_url()
        assert '/order' in current_url, (
            f'Ожидался переход на страницу заказа, текущий URL: {current_url}'
        )

    @allure.feature('Навигация')
    @allure.story('Редирект на главную страницу при клике на логотип Самоката')
    def test_scooter_logo_redirects_to_main_page(self, driver):
        """Проверяет редирект на главную страницу при клике на логотип Самоката."""
        main_page = MainPage(driver)
        
        # Переходим на другую страницу для теста редиректа
        main_page.click_header_order_button()
        
        # Кликаем на логотип и проверяем редирект
        main_page.click_on_element(MainPageLocators.header_logo_scooter)
        current_url = main_page.get_current_url()
        
        assert current_url == TestData.scooter_address, (
            f'Ожидался редирект на {TestData.scooter_address}, '
            f'текущий URL: {current_url}'
        )

    @allure.feature('Навигация')
    @allure.story('Открытие Дзена в новой вкладке при клике на логотип Яндекса')
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        """Проверяет открытие Дзена в новой вкладке при клике на логотип Яндекса."""
        main_page = MainPage(driver)
        original_tab = driver.current_window_handle
        
        main_page.click_on_element(MainPageLocators.logo_yandex)
        main_page.switch_to_next_tab()
        
        current_url = main_page.get_current_url()
        assert any(domain in current_url for domain in ['dzen.ru', 'yandex.ru']), (
            f'Ожидался переход на Дзен или Яндекс, текущий URL: {current_url}'
        )
        
        # Возвращаемся обратно и закрываем вкладку
        driver.close()
        driver.switch_to.window(original_tab)

    @allure.feature('Валидация')
    @allure.story('Проверка отображения основных элементов страницы')
    def test_main_page_elements_are_displayed(self, driver):
        """Проверяет отображение основных элементов главной страницы."""
        main_page = MainPage(driver)
        
        assert main_page.check_displaying_of_element(
            MainPageLocators.main_header
        ), 'Главный заголовок не отображается'
        
        assert main_page.check_displaying_of_element(
            MainPageLocators.faq_section
        ), 'Раздел FAQ не отображается'
        
        assert main_page.check_displaying_of_element(
            MainPageLocators.order_button_in_header
        ), 'Кнопка заказа в хедере не отображается'

    @allure.feature('Валидация')
    @allure.story('Проверка кликабельности кнопок заказа')
    def test_order_buttons_are_clickable(self, driver):
        """Проверяет, что кнопки заказа кликабельны."""
        main_page = MainPage(driver)
        
        header_button = main_page.wait_visibility_of_element(
            MainPageLocators.order_button_in_header
        )
        assert header_button.is_enabled(), 'Кнопка заказа в хедере не кликабельна'
        
        main_page.scroll_to_element(MainPageLocators.order_button_in_main)
        main_button = main_page.wait_visibility_of_element(
            MainPageLocators.order_button_in_main
        )
        assert main_button.is_enabled(), 'Кнопка заказа в основном разделе не кликабельна'