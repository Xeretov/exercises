from movie import Movie

class Action(Movie):

    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genre: str = "Action"
        self.__fine: float = 3.00
    
    def getGenre(self) -> str:
        return self.__genre
    
    def getFine(self) -> float:
        return self.__fine
    
    def calculateLateFine(self, days: int) -> float:
        return round(self.getFine() * days, 2)

class Comedy(Movie):

    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genre: str = "Comedy"
        self.__fine = 2.50
    
    def getGenre(self) -> str:
        return self.__genre
    
    def getFine(self) -> float:
        return self.__fine
    
    def calculateLateFine(self, days: int) -> float:
        return round(self.getFine() * days, 2)

class Drama(Movie):

    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genre: str = "Drama"
        self.__fine: float = 2.00
    
    def getGenre(self) -> str:
        return self.__genre
    
    def getFine(self) -> float:
        return self.__fine

    def calculateLateFine(self, days: int) -> float:
        return round(self.getFine() * days, 2)