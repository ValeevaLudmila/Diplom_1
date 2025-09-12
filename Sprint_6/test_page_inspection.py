from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def inspect_page():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    try:
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        print("🔍 Проверяем элементы на странице...")
        
        # Проверяем все input элементы
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"\n📝 Найдено input элементов: {len(inputs)}")
        for input_elem in inputs:
            placeholder = input_elem.get_attribute("placeholder") or "нет"
            id_attr = input_elem.get_attribute("id") or "нет"
            class_attr = input_elem.get_attribute("class") or "нет"
            print(f"  Input: placeholder='{placeholder}', id='{id_attr}', class='{class_attr}'")
        
        # Проверяем все div элементы с текстом
        divs = driver.find_elements(By.TAG_NAME, "div")
        print(f"\n📄 Найдено div элементов: {len(divs)}")
        for div in divs[:20]:  # Первые 20 чтобы не перегружать
            text = div.text.strip()
            if text and len(text) < 50:  # Только с текстом и не слишком длинным
                class_attr = div.get_attribute("class") or "нет"
                print(f"  Div: text='{text}', class='{class_attr}'")
                
    finally:
        driver.quit()

if __name__ == "__main__":
    inspect_page()