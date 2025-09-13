def test_debug_faq_locators(self, driver):
    """Временный тест для проверки локаторов FAQ"""
    driver.get("https://qa-scooter.praktikum-services.ru/")
    
    # Проверка основных элементов
    print("FAQ section exists:", driver.find_elements(*MainPageLocators.faq_section))
    
    # Проверка всех вопросов
    for i in range(1, 9):
        question_locator = MainPageLocators.faq_questions_items[i]
        answer_locator = MainPageLocators.faq_answers_items[i]
        
        questions = driver.find_elements(*question_locator)
        answers = driver.find_elements(*answer_locator)
        
        print(f"Question {i}: {len(questions)} elements found")
        print(f"Answer {i}: {len(answers)} elements found")
        
        if questions:
            print(f"Question text: {questions[0].text}")
        if answers:
            print(f"Answer text: {answers[0].text}")