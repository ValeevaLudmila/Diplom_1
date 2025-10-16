"""Фикстуры для тестов бургерной."""
import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def sample_bun():
    """Фикстура для создания тестовой булочки."""
    return Bun("black bun", 100.0)


@pytest.fixture
def sample_sauce():
    """Фикстура для создания тестового соуса."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)


@pytest.fixture
def sample_filling():
    """Фикстура для создания тестовой начинки."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100.0)


@pytest.fixture
def empty_burger():
    """Фикстура для создания пустого бургера."""
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture
def prepared_burger(empty_burger, sample_bun, sample_sauce, sample_filling):
    """Фикстура для создания собранного бургера."""
    empty_burger.set_buns(sample_bun)
    empty_burger.add_ingredient(sample_sauce)
    empty_burger.add_ingredient(sample_filling)
    return empty_burger