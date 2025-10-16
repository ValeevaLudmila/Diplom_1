"""Тесты для класса Bun."""
import pytest
from praktikum.bun import Bun


class TestBun:
    """Тестовый класс для булочки."""

    def test_bun_creation_sets_name_and_price(self):
        """Тест создания булочки с установкой имени и цены."""
        bun = Bun("white bun", 200.0)
        
        assert bun.name == "white bun"
        assert bun.price == 200.0

    def test_get_name_returns_correct_value(self):
        """Тест метода get_name возвращает корректное имя."""
        bun = Bun("red bun", 300.0)
        
        result = bun.get_name()
        
        assert result == "red bun"

    def test_get_price_returns_correct_value(self):
        """Тест метода get_price возвращает корректную цену."""
        bun = Bun("black bun", 100.0)
        
        result = bun.get_price()
        
        assert result == 100.0

    @pytest.mark.parametrize("name,price", [
        ("special bun", 150.5),
        ("cheese bun", 0.0),
        ("premium bun", 999.99),
    ])
    def test_bun_with_different_prices_and_names(self, name, price):
        """Параметризованный тест булочек с разными именами и ценами."""
        bun = Bun(name, price)
        
        assert bun.get_name() == name
        assert bun.get_price() == price