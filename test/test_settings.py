import unittest
from models.nomenclature import nomenclature_model
from models.recipt import recipt_model
from src.settings import settings
from src.settings_manager import settings_manager
from models.unit import unit_model
from storage.storage import storage
from logic.start_factory import start_factory

class TestSettings(unittest.TestCase):


    def test_setUp(self):
        # Подготавливаем данные для теста
        self.data = [
            nomenclature_model("Мука пшеничная", None, unit_model("кг").create_unit_kilogram()),
            nomenclature_model("Сахар", None, unit_model("кг").create_unit_kilogram()),
            nomenclature_model("Сливочное масло", None, unit_model("г").create_unit_gramm()),
            nomenclature_model("Яйца", None, unit_model("шт").create_unit_piece()),
            nomenclature_model("Ванилин", None, unit_model("г").create_unit_gramm())
        ]

    def test_create_receipt(self):
        # Подготавливаем данные для теста
        data = [
            nomenclature_model("Мука пшеничная", None, unit_model("кг").create_unit_kilogram()),
            nomenclature_model("Сахар", None, unit_model("кг").create_unit_kilogram()),
            nomenclature_model("Сливочное масло", None, unit_model("г").create_unit_gramm()),
            nomenclature_model("Яйца", None, unit_model("шт").create_unit_piece()),
            nomenclature_model("Ванилин", None, unit_model("г").create_unit_gramm())
        ]

        items1 = [{
            "Мука пшеничная": 100,
            "Сахар": 80,
            "Сливочное масло": 70,
            "Яйца": 1,
            "Ванилин": 5
        }]
        name = "Тестовый рецепт"
        comments = "Это тестовый рецепт"

        # Вызываем функцию, которую тестируем
        recipe = recipt_model.create_receipt(name, comments, items1, data)

        # Проверяем, что рецепт создан успешно
        self.assertIsInstance(recipe, recipt_model)
        self.assertEqual(recipe.name, name)
        self.assertEqual(recipe.comments, comments)
        self.assertEqual(len(recipe.rows), len(items1))

    def test_check_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()

        self.assertEqual(manager1.unique_number, manager2.unique_number)

    def test_check_json_invalid_path(self):
        # Создание экземпляра класса
        man = settings_manager()

        # Неправильный путь к файлу и проба на считывание
        file_name = "lo/other_dir/settings.json"
        self.assertIsNone(man.opener(file_name))
        self.assertEqual(man.data, {})

    def test_check_json_valid_path(self):
        # Создание экземпляра класса
        man = settings_manager()

        # Путь к файлу и проба на считывание
        file_name = "../res/settings.json"
        self.assertFalse(man.opener(file_name))
        self.assertNotEqual(man.data, {})

    def test_settings_properties_initial_values(self):
        # Создание экземпляра класса settings
        settings_obj = settings()

        # Проверка начальных значений полей
        self.assertEqual(settings_obj.BIK, "")
        self.assertEqual(settings_obj.check, "")
        self.assertEqual(settings_obj.corr_check, "")
        self.assertEqual(settings_obj.INN, "")
        self.assertEqual(settings_obj.type_of_company, "")
        self.assertEqual(settings_obj.name_of_company, "")

    def test_settings_properties_set_values(self):
        # Создание экземпляра класса settings
        settings_obj = settings()

        # Проверка сеттеров и геттеров
        settings_obj.BIK = "123456789"
        settings_obj.check = "12345678901"
        settings_obj.korr_check = "12345678901"
        settings_obj.INN = "123456789012"
        settings_obj.name_of_product = "Product A"
        settings_obj.name_of_company = "ABC Corp"

        self.assertEqual(settings_obj.BIK, "123456789")
        self.assertEqual(settings_obj.check, "12345678901")
        self.assertEqual(settings_obj.korr_check, "12345678901")
        self.assertEqual(settings_obj.INN, "123456789012")
        self.assertEqual(settings_obj.name_of_product, "Product A")
        self.assertEqual(settings_obj.name_of_company, "ABC Corp")

    def test_settings_exceptions_invalid_values(self):
        # Создание экземпляра класса settings
        settings_obj = settings()

        # Проверка исключений при некорректных данных
        with self.assertRaises(Exception):
            settings_obj.BIK = "12345678"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.check = "123456"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.korr_check = "123456"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.INN = "12345678901"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.name_of_company = "ABC"  # Некорректная длина

    def test_settings_manager_exceptions_nonexistent_file(self):
        # Попытка открыть несуществующий файл
        man = settings_manager()
        with self.assertRaises(Exception):
            man.opener("nonexistent_file.json")

    def test_settings_manager_exceptions_invalid_settings_file(self):
        # Попытка открыть файл с некорректным форматом данных
        man = settings_manager()
        with self.assertRaises(Exception):
            man.opener("invalid_settings.json")

    def test_settings_manager_opener_type(self):
        # Проверка типа возвращаемого значения метода opener
        man = settings_manager()
        self.assertIsInstance(man.opener("settings.json"), bool)

    def test_settings_manager_singleton(self):
        # Проверка, что менеджер настроек является синглтоном
        manager1 = settings_manager()
        manager2 = settings_manager()
        self.assertIs(manager1, manager2)

    def test_settings_opener_invalid_argument(self):
        # Проверка выброса исключения при передаче некорректного аргумента в метод opener
        man = settings_manager()
        with self.assertRaises(Exception):
            man.opener("123")

    def test_check_factory(self):
        unit = unit_model.create_unit_kilogram()
        assert unit is not None


    def test_check_create_receipts(self):
        items = start_factory.create_nomenclatures()
        assert len(items) > 0

    def test_check_create_nomenclatures(self):
        items = start_factory.create_nomenclatures()
        assert len(items) > 0

    def test_check_create_units(self):
        items = start_factory.create_units()
        assert len(items) > 0


    def test_check_create_groups(self):

        items = start_factory.create_groups()

        assert len(items) > 0


    def test_check_start_factor(self):

        manager = settings_manager()
        factory = start_factory(manager.settings)
        result = factory.create()
        if manager.settings.is_first_start == True:
            assert result == True
            assert not factory.storage is None
            assert storage.nomenclature_key in factory.storage.data

if __name__ == "__main__":
    unittest.main()
