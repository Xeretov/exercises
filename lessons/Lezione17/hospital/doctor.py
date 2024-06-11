from person import Person

class Doctor(Person):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)

        self.__specialization: str
        self.__parcel: float

        if not isinstance(specialization, str):
            self.__specialization = None
            print("The specialization given is not a string!")
        else:
            self.__specialization = specialization

        if not isinstance(parcel, float):
            self.__parcel = None
            print("The parcel given is not a float!")
        elif parcel > 0:
            self.__parcel = parcel
        else:
            print("The parcel given needs to be more than 0!")
        
    def setSpecialization(self, specialization: str) -> None:
        if not isinstance(specialization, str):
            print("The specialization given is not a string!")
        else:
            self.__specialization = specialization
    
    def setParcel(self, parcel: float) -> None:
        if not isinstance(parcel, float):
            print("The parcel given is not a float!")
        elif parcel > 0:
            self.__parcel = parcel
        else:
            print("The parcel given needs to be more than 0!")
    
    def getSpecialization(self) -> str:
        return self.__specialization
    
    def getParcel(self) -> float:
        return self.__parcel

    def isAValidDoctor(self) -> bool:
        if self.__age >= 30:
            print(f"Doctor {self.getName()} {self.getLastName()} is valid!")
            return True
        else:
            print(f"Doctor {self.getName()} {self.getLastName()} is not valid!")
            return False
    
    def doctorGreet(self) -> str:
        message: str
        message += super().greet()
        message += print(f" I'm a doctor specialized in {self.getSpecialization()}!")
        return message
