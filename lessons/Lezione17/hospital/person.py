class Person:

    def __init__(self, first_name: str, last_name: str) -> None:
        self.__first_name: str
        self.__last_name: str
        self.__age: int

        if not isinstance(first_name, str):
            self.__first_name = None
            print("The first name given needs to be a string!")
        else:
            self.__first_name = first_name

        if not isinstance(last_name, str):
            self.__last_name = None
            print("The last name given needs to be a string!")
        else:
            self.__last_name = last_name

        if self.__first_name and self.__last_name:
            self.__age = 0
        else:
            self.__age = None
    
    def setName(self, first_name: str) -> None:
        if not isinstance(first_name, str):
            print("The first name is not a string!")
        else:
            self.__first_name = first_name
    
    def SetLastName(self, last_name: str) -> None:
        if not isinstance(last_name, str):
            print("The last name is not a string!")
        else:
            self.__last_name = last_name
    
    def setAge(self, age: int) -> None:
        if not isinstance(age, int):
            print("Age needs to be an int!")
        elif age < 0:
            print("Age must be a positive number!")
        else:
            self.__age = age
    
    def getName(self) -> str:
        return self.__first_name

    def getLastName(self) -> str:
        return self.__last_name

    def getAge(self) -> int:
        return self.__age
    
    def greet(self) -> str:
        return f"Hello, I'm {self.getName()} {self.getLastName()}! I'm {self.getAge()}!"
