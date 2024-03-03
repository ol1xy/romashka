from src.reference import reference
from models.recipt_row import recipt_row_model
from src.errors import exception_proxy


class recipt_model(reference):
    __brutto: int = 0
    __netto: int = 0
    __rows = {}

    def add(self, row: recipt_row_model):
        exception_proxy.is_valide(row, recipt_row_model)
        self.__rows[row.name] = row
        self.__calc_brutto()

    def delete(self, row: recipt_row_model):
        exception_proxy.is_valide(row, recipt_row_model)

        if row.name in self.__rows.keys():
            self.__rows.pop(row.name)

        self.__calc_brutto()

    def __calc_brutto(self):
        self.__brutto = 0
        for position in self.__rows:
            self.__brutto += self.__rows[position].size

    @property
    def netto(self):
        return self.__netto

    @netto.setter
    def netto(self, value: int):
        exception_proxy.is_valide(value, int)

        self.__netto = value

    @staticmethod
    def create_receipt(name: str, comments: str, items: list, data: list):
        exception_proxy.is_valide(name, str)
        if not items:
            raise ValueError(f"Некорректно передан параметр {items}. Список пуст!")

        nomenclatures = reference.create_dictionary(data)

        result = []

        for position in items:
            if not position:
                raise ValueError("Невозможно сформировать элементы рецепта! Некорректный список исходных элементов!")

            nomenclature_name, size = next(iter(position.items()))

            if not nomenclature_name or not size:
                raise ValueError("Невозможно сформировать элемент рецепта. Длина кортежа не корректна!")

            nomenclature = nomenclatures[nomenclature_name]

            if nomenclature_name not in nomenclatures:
                raise ValueError(f"Некоректно передан список. Не найдена номенклатура {nomenclature_name}!")



            unit = nomenclature.unit.base_unit if nomenclature.unit.base_unit is not None else nomenclature.unit

            # Создаем запись в рецепте
            row = recipt_row_model(nomenclature, size, unit)
            result.append(row)

        return result