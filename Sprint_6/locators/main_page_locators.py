from selenium.webdriver.common.by import By

class MainPageLocators:
    main_header = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')
    faq_section = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')
    
    # Основные локаторы кнопок заказа
    order_button_in_main = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'])[last()]")
    order_button_in_header = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    
    # Альтернативные локаторы (добавьте эти строки)
    order_button_in_header_alt = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    order_button_in_main_alt = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    header_logo_scooter = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    logo_yandex = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    
    faq_questions_items = {
        1: (By.XPATH, "//div[@aria-controls='accordion__panel-24']"),
        2: (By.XPATH, "//div[@aria-controls='accordion__panel-25']"),
        3: (By.XPATH, "//div[@aria-controls='accordion__panel-26']"),
        4: (By.XPATH, "//div[@aria-controls='accordion__panel-27']"),
        5: (By.XPATH, "//div[@aria-controls='accordion__panel-28']"),
        6: (By.XPATH, "//div[@aria-controls='accordion__panel-29']"),
        7: (By.XPATH, "//div[@aria-controls='accordion__panel-30']"),
        8: (By.XPATH, "//div[@aria-controls='accordion__panel-31']")
    }

    faq_answers_items = {
        1: (By.XPATH, "//div[@id='accordion__panel-24']"),
        2: (By.XPATH, "//div[@id='accordion__panel-25']"),
        3: (By.XPATH, "//div[@id='accordion__panel-26']"),
        4: (By.XPATH, "//div[@id='accordion__panel-27']"),
        5: (By.XPATH, "//div[@id='accordion__panel-28']"),
        6: (By.XPATH, "//div[@id='accordion__panel-29']"),
        7: (By.XPATH, "//div[@id='accordion__panel-30']"),
        8: (By.XPATH, "//div[@id='accordion__panel-31']")
    }

    ORDER_BUTTON_IN_HEADER = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_IN_HEADER_ALT = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ANY_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")