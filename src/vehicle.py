
class Vehicle:

    @property
    def id(self) -> str:
        return self.__id
    
    @id.setter
    def id(self, value: str) -> None:
        self.__id = value
    
    @property
    def brand(self) -> str:
        return self.__brand
    
    @brand.setter
    def brand(self, value: str) -> None:
        self.__brand = value
    
    @property
    def model(self) -> str:
        return self.__model
    
    @model.setter
    def model(self, value: str) -> None:
        self.__model = value
    
    @property
    def mileage(self) -> int:
        return self.__mileage
    
    @mileage.setter
    def mileage(self, value: int) -> None:
        self.__mileage = value if value > 0 else -value
    
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, value: float) -> None:
        self.__price = value if value > 0 else -value
    
    def __init__(self, **kwargs) -> None:
        self.__id = kwargs.get('id')
        self.__brand = kwargs.get('brand')
        self.__model = kwargs.get('model')
        self.__mileage = kwargs.get('mileage') if kwargs.get('mileage') is not None else 0
        self.__price = kwargs.get('price') if kwargs.get('price') is not None else 0
    
    def information(self):
        return """
            id: {0}
            marca: {1}
            modelo: {2}
            kilometraje: {3}
            precio: {4}
        """.format(
            self.id, 
            self.brand, 
            self.model, 
            self.mileage, 
            self.price
        ).upper()