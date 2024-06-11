from patient import Patient
from doctor import Doctor

class Invoice:

    def __init__(self, patients: list[Patient], doctor: Doctor) -> None:
        self.patients: list[Patient]
        self.doctor: Doctor
        self.__invoice: int
        self.__salary: int

        if doctor.isAValidDoctor():
            self.patients = patients
            self.__invoice = len(self.patients)
            self.__salary = 0
            self.doctor = doctor
        else:
            self.patients, self.__invoice, self.__salary, self.doctor = None, None, None, None
            print("It's impossible to create the class invoice because the doctor is not valid!")
        
    def getSalary(self) -> int:
        self.__salary = round(self.doctor.getParcel() * self.getInvoice())
        return self.__salary

    def getInvoice(self) -> int:
        self.__invoice = len(self.patients)
        return self.__invoice

    def addPatient(self, newPatient: Patient) -> str:
        self.patients.append(newPatient)
        self.getSalary()
        return f"To the list of patients assinged to Doctor {self.doctor.getLastName()} has been added {newPatient.getIdCode()}"
    
    def removePatient(self, idCode: str) -> str:
        not_found = True
        for i,patient in enumerate(self.patients):
            if patient.getIdCode() == idCode:
                not_found = False
                del self.patients[i]
                break

        if not_found:
            return f"Id code {idCode} has not been found in Doctor {self.doctor.getLastName()}'s patients list"
        
        self.getSalary()
        return f"To the list of patients assigned to Doctor {self.doctor.getLastName()} has been removed {idCode}"
        