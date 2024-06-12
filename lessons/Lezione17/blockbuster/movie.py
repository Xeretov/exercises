class Movie:

    def __init__(self, id: int, title: str) -> None:
        self.__id: int = id
        self.__title: str = title
    
    def setID(self, id: int) -> None:
        self.__id = id
    
    def setTitle(self, title: str) -> None:
        self.__title: str = title
    
    def getID(self) -> int:
        return self.__id

    def getTitle(self) -> str:
        return self.__title
    
    def isEqual(self, otherMovie: 'Movie') -> bool:
        return True if self.getID() == otherMovie.getID() else False