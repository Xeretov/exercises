import unittest
from hospital.person import Person
from hospital.doctor import Doctor
from hospital.invoice import Invoice
from hospital.patient import Patient


class TestPerson(unittest.TestCase):

    def setUp(self) -> None:
        self.person1: Person = Person("Giuseppe","Guttoriello")
        self.person2: Person = Person(1312, (00,00))
    
    def test_initialization(self) -> None:
        self.assertEqual(self.person1.greet(), "Hello, I'm Giuseppe Guttoriello! I'm 0!")
        self.assertIsNone(self.person2.getName())
        self.assertIsNone(self.person2.getLastName())
        self.assertIsNone(self.person2.getAge())
    
    def test_setters(self) -> None:
        self.person2.setName("Angelo")
        self.person2.SetLastName(00)
        self.person2.setAge(-20)
        self.assertEqual(self.person2.greet(), "Hello, I'm Angelo None! I'm None!", "Remember that a person cannot have negative years!")

class TestDoctor(unittest.TestCase):

    def setUp(self) -> None:
        self.doctor1: Doctor = Doctor("Claudio", "D'Emilio", "chirurgy", 132.38)
        self.doctor2: Doctor = Doctor("Simone", "Piromalli", 666, "plam")
    
    def test_initialization(self) -> None:
        self.assertEqual(self.doctor1.doctorGreet(), "Hello, I'm Claudio D'Emilio! I'm 0! I'm a doctor specialized in chirurgy!")
        self.assertIsNone(self.doctor2.getSpecialization())
        self.assertIsNone(self.doctor2.getParcel())
        
    def test_setters(self) -> None:
        self.doctor2.setSpecialization("pediatric")
        self.doctor2.setParcel(-32.6)
        self.assertEqual(self.doctor2.getSpecialization(), "pediatric")
        self.assertIsNone(self.doctor2.getParcel())
        self.assertFalse(self.doctor1.isAValidDoctor())
        self.doctor1.setAge(28)
        self.assertFalse(self.doctor1.isAValidDoctor())
        self.doctor1.setAge(42)
        self.assertTrue(self.doctor1.isAValidDoctor())

class TestPatient(unittest.TestCase):

    def setUp(self) -> None:
        self.patient1: Patient = Patient("Marco", "Fragola", "Strawberry01")
    
    def test_initialization(self) -> None:
        self.assertEqual(self.patient1.patientInfo(), "Patient: Marco Fragola\nID: Strawberry01")
    
    def test_setters(self) -> None:
        self.patient1.setIdCode("STW01")
        self.assertEqual(self.patient1.getIdCode(), "STW01")


class TestInvoice(unittest.TestCase):

    def setUp(self) -> None:
        self.patient1: Patient = Patient("Marco", "Fragola", "STW01")
        self.patient2: Patient = Patient("Simone", "Pirmoalli", "CdL01")
        self.patient3: Patient = Patient("Mauro","Battista","Push01")
        self.doctor1: Doctor = Doctor("Claudio","D'Emilio","chirurgy",150.0)
        self.doctor1.setAge(35)
        self.doctor2: Doctor = Doctor("Laura","Fortuna","pediatric",70.0)
        self.doctor2.setAge(26)
        self.invoice1: Invoice = Invoice([self.patient1, self.patient2], self.doctor1)
        self.invoice2: Invoice = Invoice([self.patient1], self.doctor2)
    
    def test_initialization(self) -> None:
        self.assertEqual(self.invoice1.patients, [self.patient1, self.patient2])
        self.assertEqual(self.invoice1.doctor, self.doctor1)
        self.assertIsNone(self.invoice2.doctor)
    
    def test_getters(self) -> None:
        self.assertEqual(self.invoice1.getInvoice(), 2)
        self.assertEqual(self.invoice1.getSalary(), 300)
    
    def test_setters(self) -> None:
        self.invoice1.addPatient(self.patient3)
        self.assertEqual(self.invoice1.getInvoice(), 3)
        self.invoice1.removePatient("STW01")
        self.invoice1.removePatient("CdL01")
        self.assertEqual(self.invoice1.getInvoice(), 1)

if __name__ == "__main__":
    loader = unittest.TestLoader()
    start_dir = 'lessons/Lezione17/test'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)