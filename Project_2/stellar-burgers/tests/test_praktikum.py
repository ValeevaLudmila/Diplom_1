"""Тесты для основного модуля praktikum.py."""
import pytest
from unittest.mock import patch, Mock
import sys
import io
from praktikum.praktikum import main


class TestPraktikum:
    """Тестовый класс для основного модуля."""

    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    @patch('builtins.print')
    def test_main_function_executes_complete_flow(self, mock_print, mock_burger_class, mock_database_class):
        """Тест функция main выполняет полный поток создания бургера."""
        mock_database = Mock()
        mock_burger = Mock()
        
        mock_bun_1 = Mock()
        mock_bun_2 = Mock() 
        mock_bun_3 = Mock()
        mock_database.available_buns.return_value = [mock_bun_1, mock_bun_2, mock_bun_3]
        
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        mock_ingredient_4 = Mock()
        mock_ingredient_5 = Mock()
        mock_ingredient_6 = Mock()
        mock_database.available_ingredients.return_value = [
            mock_ingredient_1, mock_ingredient_2, mock_ingredient_3,
            mock_ingredient_4, mock_ingredient_5, mock_ingredient_6
        ]
        
        mock_burger.get_receipt.return_value = "Тестовый чек бургера"
        
        mock_database_class.return_value = mock_database
        mock_burger_class.return_value = mock_burger

        main()

        # 1. Проверяем создание объектов
        mock_database_class.assert_called_once()
        mock_burger_class.assert_called_once()
        
        # 2. Проверяем получение данных из базы
        mock_database.available_buns.assert_called_once()
        mock_database.available_ingredients.assert_called_once()
        
        # 3. Проверяем сборку бургера
        mock_burger.set_buns.assert_called_once_with(mock_bun_1)
        
        # 4. Проверяем добавление ингредиентов в правильном порядке
        expected_ingredient_calls = [
            ((mock_ingredient_2,),),
            ((mock_ingredient_5,),),
            ((mock_ingredient_4,),),
            ((mock_ingredient_6,),)
        ]
        assert mock_burger.add_ingredient.call_count == 4
        assert mock_burger.add_ingredient.call_args_list == expected_ingredient_calls
        
        # 5. Проверяем перемещение ингредиента
        mock_burger.move_ingredient.assert_called_once_with(2, 1)
        
        # 6. Проверяем удаление ингредиента
        mock_burger.remove_ingredient.assert_called_once_with(3)
        
        # 7. Проверяем получение и вывод чека
        mock_burger.get_receipt.assert_called_once()
        mock_print.assert_called_once_with("Тестовый чек бургера")

    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    def test_main_uses_correct_ingredient_indices(self, mock_burger_class, mock_database_class):
        """Тест функция main использует правильные индексы ингредиентов."""
        mock_database = Mock()
        mock_burger = Mock()
        
        mock_ingredients = [Mock() for _ in range(6)]
        mock_database.available_ingredients.return_value = mock_ingredients
        mock_database.available_buns.return_value = [Mock()]
        
        mock_database_class.return_value = mock_database
        mock_burger_class.return_value = mock_burger

        main()

        # ingredients[1] - второй ингредиент (индекс 1)
        mock_burger.add_ingredient.assert_any_call(mock_ingredients[1])
        # ingredients[4] - пятый ингредиент (индекс 4)
        mock_burger.add_ingredient.assert_any_call(mock_ingredients[4])
        # ingredients[3] - четвертый ингредиент (индекс 3)  
        mock_burger.add_ingredient.assert_any_call(mock_ingredients[3])
        # ingredients[5] - шестой ингредиент (индекс 5)
        mock_burger.add_ingredient.assert_any_call(mock_ingredients[5])

    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    @patch('builtins.print')
    def test_main_execution_flow_order(self, mock_print, mock_burger_class, mock_database_class):
        """Тест правильный порядок выполнения операций в main."""
        mock_database = Mock()
        mock_burger = Mock()
        mock_database.available_buns.return_value = [Mock()]
        mock_database.available_ingredients.return_value = [Mock() for _ in range(6)]
        mock_burger.get_receipt.return_value = "Чек"
        
        mock_database_class.return_value = mock_database
        mock_burger_class.return_value = mock_burger

        main()

        call_order = [
            mock_database_class.call_args,           # 1. Создание Database
            mock_burger_class.call_args,             # 2. Создание Burger
            mock_database.available_buns.call_args,  # 3. Получение булочек
            mock_database.available_ingredients.call_args,  # 4. Получение ингредиентов
            mock_burger.set_buns.call_args,          # 5. Установка булочки
        ]
        
        assert mock_database_class.called
        assert mock_burger_class.called
        assert mock_database.available_buns.called
        assert mock_database.available_ingredients.called
        assert mock_burger.set_buns.called

    def test_main_module_can_be_imported_and_has_main_function(self):
        """Тест модуль может быть импортирован и содержит функцию main."""
        from praktikum import praktikum
        
        assert hasattr(praktikum, 'main')
        assert callable(praktikum.main)
        
        assert hasattr(praktikum, '__name__')

    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger') 
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_prints_to_stdout(self, mock_stdout, mock_burger_class, mock_database_class):
        """Тест функция main печатает в stdout."""
        mock_database = Mock()
        mock_burger = Mock()
        mock_database.available_buns.return_value = [Mock()]
        mock_database.available_ingredients.return_value = [Mock() for _ in range(6)]
        mock_burger.get_receipt.return_value = "Содержимое чека"
        
        mock_database_class.return_value = mock_database
        mock_burger_class.return_value = mock_burger

        main()

        assert mock_stdout.getvalue() == "Содержимое чека\n"