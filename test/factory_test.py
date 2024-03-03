from models.unit import unit_model
from logic.start_factory import start_factory
from src.settings_manager import settings_manager
from storage.storage import storage

import unittest


#
# Набор автотестов для проверки работы фабричного метода
#
class factory_test(unittest.TestCase):
    """
     Проверка создания ед. измерения
    """
    def test_check_factory(self):
        unit = unit_model.create_unit_kilogram()
        assert unit is not None

    """
     Проверка создания начальных рецептов
    """
    def test_check_create_receipts(self):

        items = start_factory.create_receipts()
        assert len(items) > 0


    """Проверка создание начальной номенклатуры"""
    def test_check_create_nomenclatures(self):

        items = start_factory.create_nomenclatures()
        assert len(items) > 0

    "Проверка создание списка единиц измерения"
    def test_check_create_units(self):
        items = start_factory.create_units()
        assert len(items) > 0

    """Проверка создания списка групп"""
    def test_check_create_groups(self):

        items = start_factory.create_groups()

        assert len(items) > 0


    """ Проверка работы класса start_factory """

    def test_check_start_factor(self):
        # Подготовка
        manager = settings_manager()
        factory = start_factory(manager.settings)

        # Действие
        result = factory.create()

        # Проверка
        if manager.settings.is_first_start == True:
            assert result == True
            assert not factory.storage is None
            assert storage.nomenclature_key in factory.storage.data
