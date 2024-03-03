class storage:
    __data = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance

    @property
    def data(self) -> dict:
        return self.__data

    @staticmethod
    def nomenclature_key():
        return "nomenclatures"

    @staticmethod
    def group_key():
        return "groups"

    @staticmethod
    def unit_key():
        return "units"

    @staticmethod
    def receipt_key():
        return "receipts"