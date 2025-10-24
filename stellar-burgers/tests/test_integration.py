"""Интеграционные тесты сборки бургера."""
import pytest
from praktikum.burger import Burger
from praktikum.database import Database


class TestBurgerAssembly:
    """Интеграционные тесты сборки бургера."""

    def test_complete_burger_creation_flow(self):
        """Тест полного процесса создания бургера."""
        db = Database()
        burger = Burger()
        
        buns = db.available_buns()
        ingredients = db.available_ingredients()
        
        selected_bun = buns[0]  # black bun
        selected_sauce = ingredients[0]  # hot sauce
        selected_filling = ingredients[3]  # cutlet
        
        burger.set_buns(selected_bun)
        burger.add_ingredient(selected_sauce)
        burger.add_ingredient(selected_filling)
        
        expected_price = selected_bun.get_price() * 2 + selected_sauce.get_price() + selected_filling.get_price()
        actual_price = burger.get_price()
        
        assert actual_price == expected_price
        
        receipt = burger.get_receipt()
        assert selected_bun.get_name() in receipt
        assert selected_sauce.get_name() in receipt
        assert selected_filling.get_name() in receipt
        assert str(expected_price) in receipt

    def test_burger_manipulation_operations(self):
        """Тест операций манипуляции с бургером."""
        db = Database()
        burger = Burger()
        
        buns = db.available_buns()
        ingredients = db.available_ingredients()
        
        burger.set_buns(buns[1])  # white bun
        
        burger.add_ingredient(ingredients[0])  # hot sauce
        burger.add_ingredient(ingredients[3])  # cutlet
        burger.add_ingredient(ingredients[4])  # dinosaur
        
        initial_price = burger.get_price()
        
        burger.move_ingredient(0, 2)
        
        assert burger.get_price() == initial_price
        
        burger.remove_ingredient(1)
        
        assert burger.get_price() < initial_price