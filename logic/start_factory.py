from models.group import group_model
from models.unit import unit_model
from models.nomenclature import nomenclature_model
from src.reference import reference
from models.recipt import recipt_model
from src.settings import settings
from storage.storage import storage
from src.errors import exception_proxy, operation_exception


class start_factory:
    __options: settings = None
    __storage: storage = None

    def __init__(self, __options: settings, __storage: storage = None) -> None:

        exception_proxy.is_valide(__options, settings)
        self.__options = __options
        self.__storage = __storage

    def __save(self, key: str, items: list):
        exception_proxy.is_valide(key, str)

        if self.__storage is None:
            self.__storage = storage()

        self.__storage.data[key] = items

    @property
    def storage(self):
        return self.__storage

    @staticmethod
    def create_units():
        items = []
        items.append(unit_model.create_unit_gramm())
        items.append(unit_model.create_unit_kilogram())
        items.append(unit_model.create_unit_litr())
        items.append(unit_model.create_unit_millilitr())
        items.append(unit_model.create_unit_piece())

        return items

    @staticmethod
    def create_nomenclatures():
        group = group_model.create_default_group()
        items = {"Мука пшеничная": "кг",
                 "Сахар": "кг",
                 "Сливочное масло": "кг",
                 "Корица": "гр",
                 "Какао": "кг",
                 "Яйца": "шт",
                 "Ванилин": "гр",
                 "Куриное филе": "кг",
                 "Салат Романо": "гр",
                 "Сыр Пармезан": "кг",
                 "Чеснок": "кг",
                 "Белый хлеб": "кг",
                 "Соль": "кг",
                 "Черный перец": "гр",
                 "Оливковое масло": "л",
                 "Лимонный сок": "л",
                 "Горчица дижонская": "гр",
                 "Сахарная пудра": "гр",
                 "Ванилиин": "гр"}

        units = reference.create_dictionary(start_factory.create_units())

        result = []
        for position in items:
            __list = [position, items[position]]
            if len(__list) < 1:
                raise operation_exception(
                    "Невозможно сформировать элементы номенклатуры! Некорректный список исходных элементов!")

            name = __list[0]
            unit_name = __list[1]


            item = nomenclature_model(name, group, units[unit_name])
            result.append(item)


        return result

    @staticmethod
    def create_groups():
        items = []
        items.append(group_model.create_default_group())
        return items

    @staticmethod
    def create_receipts():
        result = []
        data = start_factory.create_nomenclatures()

        #Вафли хрустящие в вафельнице
        items = [{"Мука пшеничная": 100,
                 "Сахар": 80,
                 "Сливочное масло": 70,
                 "Яйца": 1,
                 "Ванилин": 5}]
        result.append(recipt_model.create_receipt("Вафли хрустящие в вафельнице", "", items, data))

        # Цезарь с курицей
        items = [{"Куриное филе": 200,
                 "Салат Романо": 50,
                 "Сыр Пармезан": 50,
                 "Чеснок": 10,
                 "Белый хлеб": 30,
                 "Соль": 5,
                 "Черный перец": 2,
                 "Оливковое масло": 10,
                 "Лимонный сок": 5,
                 "Горчица дижонская": 5,
                 "Яйца": 2}]
        result.append(recipt_model.create_receipt("Цезарь с курицей", "", items, data))

        # Безе
        items = [{"Яйца": 3,
                 "Сахарная пудра": 180,
                 "Ванилиин": 5,
                 "Корица": 5,
                 "Какао": 20}]
        result.append(recipt_model.create_receipt("Безе", "", items, data))

        return result

    def create(self) -> bool:
        if self.__options.is_first_start:
            self.__options.is_first_start = False

            items = start_factory.create_nomenclatures()
            self.__save(storage.nomenclature_key(), items)

            items = start_factory.create_units()
            self.__save(storage.unit_key(), items)

            items = start_factory.create_groups()
            self.__save(storage.group_key(), items)

            items = start_factory.create_receipts()
            self.__save(storage.receipt_key(), items)

        else:
            return True
