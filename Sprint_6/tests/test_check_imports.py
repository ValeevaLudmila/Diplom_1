import sys
import os

# Добавляем путь к корневой директории проекта
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("🔍 Проверка импортов...")

try:
    from pages.main_page import MainPage
    print("✅ MainPage импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта MainPage: {e}")

try:
    from pages.order_page import OrderPage
    print("✅ OrderPage импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта OrderPage: {e}")

try:
    from pages.base_page import BasePage
    print("✅ BasePage импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта BasePage: {e}")

try:
    from locators.order_page_locators import OrderPageLocators
    print("✅ OrderPageLocators импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта OrderPageLocators: {e}")

try:
    from locators.main_page_locators import MainPageLocators
    print("✅ MainPageLocators импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта MainPageLocators: {e}")

try:
    from data import TestData
    print("✅ TestData импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта TestData: {e}")

try:
    from webdriver_manager.firefox import GeckoDriverManager
    print("✅ GeckoDriverManager импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта GeckoDriverManager: {e}")

try:
    import allure
    print("✅ allure импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта allure: {e}")