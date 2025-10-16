"""Тесты для класса Burger."""
import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:
    """Тестовый класс для бургера."""

    def test_burger_initialization_creates_empty_burger(self, empty_burger):
        """Тест инициализации создает пустой бургер."""
        assert empty_burger.bun is None
        assert empty_burger.ingredients == []

    def test_set_buns_sets_bun_correctly(self, empty_burger, sample_bun):
        """Тест установки булочки в бургер."""
        empty_burger.set_buns(sample_bun)
        
        assert empty_burger.bun == sample_bun

    def test_add_ingredient_adds_to_ingredients_list(self, empty_burger, sample_sauce):
        """Тест добавления ингредиента в бургер."""
        empty_burger.add_ingredient(sample_sauce)
        
        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] == sample_sauce

    @pytest.mark.parametrize("num_ingredients", [1, 3, 5])
    def test_add_multiple_ingredients_increases_count(self, empty_burger, num_ingredients):
        """Тест добавления нескольких ингредиентов увеличивает счетчик."""
        for i in range(num_ingredients):
            ingredient = Mock(spec=Ingredient)
            ingredient.get_name.return_value = f"ingredient_{i}"
            empty_burger.add_ingredient(ingredient)
        
        assert len(empty_burger.ingredients) == num_ingredients

    def test_remove_ingredient_decreases_ingredients_count(self, prepared_burger):
        """Тест удаления ингредиента уменьшает счетчик."""
        initial_count = len(prepared_burger.ingredients)
        prepared_burger.remove_ingredient(0)
        
        assert len(prepared_burger.ingredients) == initial_count - 1

    def test_remove_ingredient_with_invalid_index_raises_error(self, empty_burger):
        """Тест удаления с невалидным индексом вызывает ошибку."""
        with pytest.raises(IndexError):
            empty_burger.remove_ingredient(0)

    def test_move_ingredient_changes_position(self, prepared_burger):
        """Тест перемещения ингредиента изменяет позицию."""
        first_ingredient = prepared_burger.ingredients[0]
        second_ingredient = prepared_burger.ingredients[1]
        
        prepared_burger.move_ingredient(0, 1)
        
        assert prepared_burger.ingredients[0] == second_ingredient
        assert prepared_burger.ingredients[1] == first_ingredient

    @pytest.mark.parametrize("index_from,index_to", [(0, 2), (2, 0), (1, 1)])
    def test_move_ingredient_different_positions(self, index_from, index_to):
        """Тест перемещения ингредиента между разными позициями."""
        burger = Burger()
        ingredients = [Mock(), Mock(), Mock()]
        burger.ingredients = ingredients.copy()
        
        burger.move_ingredient(index_from, index_to)
        
        moved_ingredient = ingredients[index_from]
        assert burger.ingredients[index_to] == moved_ingredient

    def test_get_price_calculates_correct_total(self, prepared_burger):
        """Тест расчета цены возвращает корректную сумму."""
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100.0
        
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 50.0
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 75.0
        
        prepared_burger.bun = mock_bun
        prepared_burger.ingredients = [mock_ingredient1, mock_ingredient2]
        
        result = prepared_burger.get_price()
        
        expected_price = 100.0 * 2 + 50.0 + 75.0
        assert result == expected_price

    def test_get_price_without_bun_returns_ingredients_price(self, empty_burger):
        """Тест расчета цены без булочки вызывает ошибку (т.к. bun обязателен)."""
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 100.0
        empty_burger.add_ingredient(mock_ingredient)
    
        with pytest.raises(AttributeError, match="'NoneType' object has no attribute 'get_price'"):
            empty_burger.get_price()

    def test_get_price_without_ingredients_returns_bun_price_only(self, empty_burger):
        """Тест расчета цены без ингредиентов возвращает только цену булочки."""
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100.0
        empty_burger.set_buns(mock_bun)
        
        result = empty_burger.get_price()
        
        assert result == 200.0

    def test_get_price_empty_burger_returns_zero(self):
        """Тест расчета цены пустого бургера возвращает ноль (с установленной булочкой)."""

        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 0.0
        burger.set_buns(mock_bun)
    
        result = burger.get_price()
    
        assert result == 0.0

    def test_get_receipt_includes_all_components(self, prepared_burger):
        """Тест генерации чека включает все компоненты."""
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = "SAUCE"
        mock_sauce.get_name.return_value = "hot sauce"
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = "FILLING"
        mock_filling.get_name.return_value = "cutlet"
        
        prepared_burger.bun = mock_bun
        prepared_burger.ingredients = [mock_sauce, mock_filling]
        
        with pytest.MonkeyPatch().context() as m:
            m.setattr(prepared_burger, 'get_price', lambda: 325.0)
            receipt = prepared_burger.get_receipt()
        
        expected_lines = [
            "(==== black bun ====)",
            "= sauce hot sauce =",
            "= filling cutlet =",
            "(==== black bun ====)",
            "",
            "Price: 325.0"
        ]
        expected_receipt = "\n".join(expected_lines)
        
        assert receipt == expected_receipt

    def test_get_receipt_without_bun_includes_price(self):
        """Тест генерации чека с булочкой включает цену."""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Тестовая булочка"
        mock_bun.get_price.return_value = 100.0
    
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "Острый соус"
        mock_ingredient.get_price.return_value = 50.0
    
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
    
        receipt = burger.get_receipt()
    
        assert "Price: 250.0" in receipt