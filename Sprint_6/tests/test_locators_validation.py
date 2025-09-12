import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestLogoYandex:
    """Тест для проверки локатора logo_yandex"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"
        self.logo_yandex_locator = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    
    def check_network(self):
        """Проверка сетевого соединения"""
        try:
            response = requests.get("https://ya.ru", timeout=5)
            return response.status_code == 200
        except requests.exceptions.ConnectionError:
            return False
        except Exception:
            return False
    
    def test_logo_yandex_availability(self):
        """Тест доступности логотипа Яндекс"""
        # Пропускаем тест если нет сети
        if not self.check_network():
            pytest.skip("Нет сетевого соединения - пропускаем тест")
        
        print("Открываем главную страницу...")
        self.driver.get(self.base_url)
        
        try:
            # Ждем загрузки страницы
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("Страница загрузилась")
            
            # Проверяем логотип Яндекс
            print("Ищем логотип Яндекс...")
            logo_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.logo_yandex_locator)
            )
            
            # Проверяем отображение
            assert logo_element.is_displayed(), "Логотип Яндекс не отображается"
            print("✓ Логотип Яндекс найден и отображается")
            
            # Проверяем кликабельность
            assert logo_element.is_enabled(), "Логотип Яндекс не кликабелен"
            print("✓ Логотип Яндекс кликабелен")
            
            # Проверяем наличие href (ссылки)
            href = logo_element.get_attribute("href")
            assert href is not None, "Логотип Яндекс не имеет ссылки"
            print(f"✓ Ссылка логотипа: {href}")
            
        except TimeoutException:
            # Попробуем найти элемент без ожидания
            try:
                logo_elements = self.driver.find_elements(*self.logo_yandex_locator)
                if logo_elements:
                    logo_element = logo_elements[0]
                    if logo_element.is_displayed():
                        print("✓ Логотип Яндекс найден (без ожидания)")
                        return
                
                pytest.fail("Логотип Яндекс не найден даже после таймаута")
                
            except Exception as e:
                pytest.fail(f"Ошибка при поиске логотипа Яндекс: {e}")
                
        except Exception as e:
            pytest.fail(f"Неожиданная ошибка: {e}")
    
    def test_logo_yandex_clickable(self):
        """Тест кликабельности логотипа Яндекс"""
        if not self.check_network():
            pytest.skip("Нет сетевого соединения")
        
        self.driver.get(self.base_url)
        
        try:
            logo_element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.logo_yandex_locator)
            )
            
            # Сохраняем текущее окно
            main_window = self.driver.current_window_handle
            
            # Кликаем на логотип
            logo_element.click()
            print("Кликнули на логотип Яндекс")
            
            # Ждем открытия новой вкладки
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.window_handles) > 1
            )
            
            # Переключаемся на новую вкладку
            new_window = [window for window in self.driver.window_handles if window != main_window][0]
            self.driver.switch_to.window(new_window)
            
            # Проверяем, что открылась страница Яндекс
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("yandex")
            )
            
            print("✓ Логотип Яндекс кликабелен и открывает новую вкладку")
            
            # Закрываем новую вкладку и возвращаемся
            self.driver.close()
            self.driver.switch_to.window(main_window)
            
        except Exception as e:
            pytest.fail(f"Логотип Яндекс не кликабелен: {e}")