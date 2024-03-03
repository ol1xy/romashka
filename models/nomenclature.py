from src.reference import reference
from src.errors import exception_proxy


class nomenclature_model(reference):
    __group = None
    __unit = None

    def __init__(self, name: str, group: reference = None, unit: reference = None):
        self.error = exception_proxy()
        self.__group = group
        self.__unit = unit
        super().__init__(name)

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value: reference):
        exception_proxy.is_valide(value, reference)
        self.__group = value

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value: reference):
        exception_proxy.is_valide(value, reference)
        self.__unit = value

    # Геттер и сеттер для поля full_name
    @property
    def name_of_product(self):
        return self.__full_name

    @name_of_product.setter
    def name_of_product(self, value: str):
        if len(value) > 255:
            self.error.set_error_source("Превышена максимальная длина для полного наименования!", self)
        self.__full_name = value