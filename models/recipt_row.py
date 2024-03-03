from src.reference import reference
from models.nomenclature import nomenclature_model
from models.unit import unit_model
from src.errors import exception_proxy


#
# Класс описание строки рецепта
#
class recipt_row_model(reference):
    __nomenclature: nomenclature_model = None
    __size: int = 0
    __unit: unit_model = None

    def __init__(self, __nomenclature: nomenclature_model, __size: int, __unit: unit_model):
        exception_proxy.is_valide(__nomenclature, reference)
        exception_proxy.is_valide(__unit, reference)

        self.__nomenclature = __nomenclature
        self.__size = __size
        self.__unit = __unit

        super().__init__(f"{__nomenclature.name} , {__unit.name} ")

    @property
    def nomenclature(self):
        return self.__nomenclature

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: int):
        self.__size = value

    @property
    def unit(self):
        return self.__unit