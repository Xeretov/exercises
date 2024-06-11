from person import Person

class Patient(Person):

    def __init__(self, first_name: str, last_name: str, idCode: str) -> None:
        super().__init__(first_name, last_name)
        self.__idCode: str = idCode
    
    def setIdCode(self, idCode: str) -> None:
        self.__idCode = idCode
    
    def getIdCode(self) -> None:
        return self.__idCode

    def patientInfo(self) -> str:
        message: str
        message += f"Patient: {self.getName()} {self.getLastName()}\n"
        message += f"ID: {self.getIdCode()}"
        return message