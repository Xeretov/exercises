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
        return key in self.__testo

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

    def leggiTestoDaFile(self):
        with open(self.nomePercorso, "r") as file:
            self.__testo = file.read()

    def getText(self) -> str:
        return "Percorso: " + self.nomePercorso + "\nContenuto: " + self.getTesto()


email: Email = Email("Hello,\n\nI am a Nigerian prince, I need your help to get my royal money.\nWith just 5000 euros I can access my billions, if you help me I can send you 100,000 euros.\n\nNice meeting you,\nThe nigerian prince.", "nigerianprince@gmail.com","gioeleamendola@gmail.com","Royal money")

file: File = File("Ciao Mondo!","C:\\Users\\Cloud\\Documents\\ITIS\\VSProjects\\exercises\\lessons\\Lezione24\\documentoImportante\\princip.txt")

print("\n"+email.getText(),end="\n\n")

print("\n"+file.getText(),end="\n\n")

email.writeToFile("email1.txt","C:\\Users\\Cloud\\Documents\\ITIS\\VSProjects\\exercises\\lessons\\Lezione24\\documentoImportante")

print("\nLa parola 'incontrarci' è presente nel testo dell'email? ",email.isInText("meet"),end="\n\n")

print("\nLa parola 'percorso' è presente nel testo del file?  ",file.isInText("percorso"),end="\n\n")

# ### Test con UnitTest
# Utilizzando il modulo unittest, definire i seguenti test per le classi Documento, Email e File.

 
# I test devono includere:
# Verifica dei metodi getText() e setText() nella classe Documento.
# Verifica del metodo isInText() nella classe Documento.
# Verifica del metodo getText() nella classe Email.
# Verifica del metodo writeToFile() nella classe Email.
# Verifica del metodo isInText() nella classe Email.
# Verifica del metodo getText() nella classe File.
# Verifica del metodo isInText() nella classe File.