# Gioele Amendola
# 18/07/2024

from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro: str):
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato: str):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave: int):
        self.chiave: int = chiave
    
    def __sposta_carattere(self, char: str) -> str:
        if char.isalpha():
            if char.isupper():
                return chr((ord(char) - ord('A') + self.chiave) % 26 + ord('A'))
            else:
                return chr((ord(char) - ord('a') + self.chiave) % 26 + ord('a'))
        return char

    def __decodifica_carattere(self, char: str) -> str:
        if char.isalpha():
            if char.isupper():
                return chr((ord(char) - ord('A') - self.chiave) % 26 + ord('A'))
            else:
                return chr((ord(char) - ord('a') - self.chiave) % 26 + ord('a'))
        return char

    def codifica(self, testoInChiaro: str):
        testoCodificato: str = ""
        for c in testoInChiaro:
            testoCodificato += self.__sposta_carattere(c)
        return testoCodificato

    def decodifica(self, testoCodificato: str):
        testoDecodificato: str = ""
        for c in testoCodificato:
            testoDecodificato += self.__decodifica_carattere(c)
        return testoDecodificato

    def leggi_file(self, path: str):
        with open(path, 'r') as file:
            return file.read()
    
    def scrivi_file(self, path: str, testo: str):
        with open(path, 'w') as file:
            file.write(testo)

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n: int):
        self.n: int = n
    
    def __combinazione(self, testo: str) -> str:
        if len(testo)%2 == 0:
            length: int = len(testo)//2
        else:
            length: int = len(testo)//2 + 1
        half1: str = testo[:length]
        half2: str = testo[length:]
        result: str = ""
        for i in range(len(half2)):
            result += half1[i] + half2[i]
        if len(testo)%2 != 0:
            result += half1[length-1]
        return result
    
    def __decodifica_combinazione(self, testo: str) -> str:
        length: int = len(testo)
        half1: str = ""
        half2: str = ""
        for i in range(length):
            if i % 2 == 0:
                half1 += testo[i]
            else:
                half2 += testo[i]
        return half1 + half2
    
    def codifica(self, testoInChiaro: str):
        testoCodificato: str = self.__combinazione(testoInChiaro)
        return testoCodificato
    
    def decodifica(self, testoCodificato: str):
        testoDecodificato: str = self.__decodifica_combinazione(testoCodificato)
        return testoDecodificato
    
    def leggi_file(self, path: str):
        with open(path, 'r') as file:
            return file.read()
    
    def scrivi_file(self, path: str, testo: str):
        with open(path, 'w') as file:
            file.write(testo)

if __name__ == "__main__":
    cifratoreScorrimento: CifratoreAScorrimento = CifratoreAScorrimento(3)
    testoInChiaro: str = cifratoreScorrimento.leggi_file("lessons\Lezione26\codificare.txt")
    testoCodificato: str = cifratoreScorrimento.codifica(testoInChiaro)
    cifratoreScorrimento.scrivi_file("lessons\Lezione26\codificatoScorrimento.txt", testoCodificato)
    print(testoCodificato)

    testoDecodificato: str = cifratoreScorrimento.decodifica(testoCodificato)
    print(testoDecodificato)

    cifratoreCombinazione: CifratoreACombinazione = CifratoreACombinazione(3)
    testoInChiaro = cifratoreCombinazione.leggi_file("lessons\Lezione26\codificare.txt")
    testoCodificato = cifratoreCombinazione.codifica(testoInChiaro)
    cifratoreCombinazione.scrivi_file("lessons\Lezione26\codificatoCombinazione.txt", testoCodificato)
    print(testoCodificato)

    testoDecodificato = cifratoreCombinazione.decodifica(testoCodificato)
    print(testoDecodificato)