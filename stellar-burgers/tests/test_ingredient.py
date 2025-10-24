"""Тесты для класса Ingredient."""
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тестовый класс для ингредиента."""

    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200.0),
    ])
    def test_ingredient_creation_sets_attributes(self, ingredient_type, name, price):
        """Тест создания ингредиента с установкой атрибутов."""
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price_returns_correct_value(self):
        """Тест метода get_price возвращает корректную цену."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300.0)
        
        result = ingredient.get_price()
        
        assert result == 300.0

    def test_get_name_returns_correct_value(self):
        """Тест метода get_name возвращает корректное имя."""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300.0)
        
        result = ingredient.get_name()
        
        assert result == "sausage"

    def test_get_type_returns_correct_value(self):
        """Тест метода get_type возвращает корректный тип."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        
        result = ingredient.get_type()
        
        assert result == INGREDIENT_TYPE_SAUCE

    @pytest.mark.parametrize("price", [0.0, 0.5, 100.0, 999.99])
    def test_ingredient_with_different_prices(self, price):
        """Тест ингредиентов с разными ценами."""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "test filling", price)
        
        assert ingredient.get_price() == price