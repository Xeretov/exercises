# Gioele Amendola
# 10/07/2024

class Documento:
    def __init__(self, testo):
        self.__testo = testo

    def getText(self) -> str:
        return self.__testo

    def setText(self, testo: str):
        self.__testo = testo

    def isInText(self, key: str) -> bool:
        return key.lower() in self.__testo.lower()

class Email(Documento):
    def __init__(self, testo: str, mittente: str, destinatario: str, titolo: str) -> None:
        super().__init__(testo)
        self.__mittente: str = mittente
        self.__destinatario: str = destinatario
        self.__titolo: str = titolo

    def getMittente(self) -> str:
        return self.__mittente
    def getDestinatario(self) -> str:
        return self.__destinatario
    def getTitolo(self) -> str:
        return self.__titolo
    def getTesto(self) -> str:
        return super().getText()
    
    def setMittente(self, mittente: str):
        self.__mittente = mittente
    def setDestinatario(self, destinatario: str):
        self.__destinatario = destinatario
    def setTitolo(self, titolo: str):
        self.__titolo = titolo
    def setTesto(self, testo: str):
        super().setText(testo)


    def getText(self) -> str:
        return "Da: " + self.getMittente() + ", A: " + self.getDestinatario() + "\nTitolo: " + self.getTitolo() + "\nMessaggio:\n" + self.getTesto()

    def writeToFile(self, filename: str, path: str):
        with open(path +"\\"+ filename, "w") as file:
            file.write(self.getText())
    
    def isInText(self, key: str) -> bool:
        return super().isInText(key)

class File(Documento):
    def __init__(self, testo: str, nomePercorso: str):
        super().__init__(testo)
        self.nomePercorso: str = nomePercorso

    def getTesto(self) -> str:
        return super().getText()

    def scriviTestoInFile(self):
        with open(self.nomePercorso, "w") as file:
            file.write(self.getTesto())

    def leggiTestoDaFile(self):
        with open(self.nomePercorso, "r") as file:
            self.__testo = file.read()

    def getText(self) -> str:
        return "Percorso: " + self.nomePercorso + "\nContenuto: " + self.getTesto()


email: Email = Email("Hello,\n\nI am a Nigerian prince, I need your help to get my royal money.\nWith just 5000 euros I can access my billions, if you help me I can send you 100,000 euros.\n\nNice meeting you,\nThe nigerian prince.", "nigerianprince@gmail.com","gioeleamendola@gmail.com","Royal money")

file: File = File("Ciao Mondo!","lessons\\Lezione24\\documentoImportante\\princip.txt")

print("\n"+email.getText(),end="\n\n")

print("\n"+file.getText(),end="\n\n")

email.writeToFile("email1.txt","lessons\\Lezione24\\documentoImportante")

print("\nLa parola 'incontrarci' è presente nel testo dell'email? ",email.isInText("meet"),end="\n\n")

print("\nLa parola 'percorso' è presente nel testo del file?  ",file.isInText("percorso"),end="\n\n")

# ### Test con UnitTest
# Utilizzando il modulo unittest, definire i seguenti test per le classi Documento, Email e File.
import unittest
import os
class TestDocumento(unittest.TestCase):
    def setUp(self) -> None:
        self.doc: Documento = Documento("Hello World!")

    def test_getText(self):
        self.assertEqual(self.doc.getText(),"Hello World!")
 
    def test_setText(self):
        self.doc.setText("Ciao Mondo!")
        self.assertEqual(self.doc.getText(),"Ciao Mondo!")

    def test_isInText(self):
        self.assertEqual(self.doc.isInText("hello"),True)
        self.assertEqual(self.doc.isInText("carretto"),False)

class TestEmail(unittest.TestCase):
    def setUp(self) -> None:
        self.email: Email = Email("Hello everyone!\nI'm glad to announce...","promotion@blizzard.com","julianassange@wikileaks.com","Promotion")
    
    def test_getText(self) -> None:
        self.assertEqual(self.email.getText(),"Da: promotion@blizzard.com, A: julianassange@wikileaks.com\nTitolo: Promotion\nMessaggio:\nHello everyone!\nI'm glad to announce...")
    
    def test_writeToFile(self) -> None:
        self.email.writeToFile("email.txt","lessons\\Lezione24\\documentoImportante")
        self.assertTrue(os.path.exists("lessons\\Lezione24\\documentoImportante\email.txt"))
        with open("lessons\\Lezione24\\documentoImportante\\email.txt","r") as file:
            self.assertEqual(file.read(),self.email.getText())
        os.remove("lessons\\Lezione24\\documentoImportante\email.txt")
    
    def test_isInText(self) -> None:
        self.assertEqual(self.email.isInText("everyone"),True)
        self.assertEqual(self.email.isInText("carretto"),False)

class TestFile(unittest.TestCase):
    def setUp(self) -> None:
        self.file: File = File("Hello World!","lessons\\Lezione24\\documentoImportante\\file.txt")
    
    def test_getText(self) -> None:
        self.assertEqual(self.file.getText(),"Percorso: " + "lessons\\Lezione24\\documentoImportante\\file.txt" + "\nContenuto: " + "Hello World!")
    
    def test_isInText(self) -> None:
        self.assertEqual(self.file.isInText("hello"),True)
        self.assertEqual(self.file.isInText("carretto"),False)

if __name__ == "__main__":
    unittest.main()
