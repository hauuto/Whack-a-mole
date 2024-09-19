class Car:
    def __init__(self, model: str, year: int, color: str):
        self.__model = model
        self.__year = year
        self.__color = color
        self.__numberOfColorChanges = 0

    def setModel(self, model: str) -> None:
        self.__model = model

    def getModel(self) -> str:
        return self.__model

    def setYear(self, year: int) -> None:
        self.__year = year

    def getYear(self) -> int:
        return self.__year

    def setColor(self, color: str) -> None:
        if self.__color != color:
            self.__color = color
            self.__numberOfColorChanges += 1

    def getNumberOfColorChanges(self) -> int:
        return self.__numberOfColorChanges

    # Hàm in thông tin của xe
    def print(self) -> None:
        print(f"Model: {self.__model}")
        print(f"Year: {self.__year}")
        print(f"Color: {self.__color}")
        print(f"Number of color changes: {self.__numberOfColorChanges}")
