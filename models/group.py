from src.reference import reference

#
# Модель группу номенклатуры
#
class group_model(reference):
    @staticmethod
    def create_default_group():
        item = group_model("Продукты")
        return item