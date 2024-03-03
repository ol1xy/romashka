from src.reference import reference
from src.errors import exception_proxy, argument_exception


#
# Модель единицы измерения для номенклатуры
#
class unit_model(reference):
    # Базовая единица измерения
    __base_unit: reference = None

    # Коэффициент пересчета к базовой единице измерения
    __coefficient: int = 1

    def __init__(self, name: str, base_unit: reference = None, coefficient: int = 1):
        super().__init__(name)

        if base_unit != None:
            self.__base_unit = base_unit

        if coefficient != 1:
            self.coefficient = coefficient

    @property
    def base_unit(self):
        """
            Базовая единица измерения
        Returns:
            _type_: _description_
        """
        return self.__base_unit

    @base_unit.setter
    def base(self, value: reference):
        exception_proxy.is_valide(value, reference)
        self.__base_unit = value

    @property
    def coefficient(self):
        """
            Коэффициент пересчета
        Returns:
            _type_: _description_
        """
        return self.__coefficient

    @coefficient.setter
    def coefficient(self, value: int):
        exception_proxy.is_valide(value, int)

        if (value <= 0):
            raise argument_exception("Значение коэффициента должно быть > 1!")

        self.__coefficient = value

    @staticmethod
    def create_unit_gramm():
        item = unit_model('гр', None, 1)
        return item

    @staticmethod
    def create_unit_kilogram():
        base = unit_model.create_unit_gramm()
        item = unit_model('кг', base, 1000)
        return item

    @staticmethod
    def create_unit_millilitr():
        item = unit_model('мл', None, 1)
        return item

    @staticmethod
    def create_unit_litr():
        base = unit_model.create_unit_millilitr()
        item = unit_model('л', base, 1000)
        return item

    @staticmethod
    def create_unit_piece():
        item = unit_model('шт', None, 1)
        return item