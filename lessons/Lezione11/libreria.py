# Gioele Amendola
# 29/05/2025

# Sistema Avanzato di Gestione Biblioteca

# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python.
# Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi.
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli,
# restituirli e visualizzare quali libri sono disponibili in un dato momento.

class Libro:

    def __init__(self, titolo: str, autore: str, disponibile: bool = True) -> None:
        self.titolo: str = titolo
        self.autore: str = autore
        self.disponibile: bool = disponibile

class Biblioteca:

    def __init__(self) -> None:
        self.catalogo: list[Libro] = []
    
    def aggiungi_libro(self, libro: Libro) -> str:
        self.catalogo.append(libro)
        return "Libro aggiunto con successo"
    
    def presta_libro(self, titolo: str) -> str:
        libro: Libro = [libro for libro in self.catalogo if titolo == libro.titolo][0]
        if libro:
            if libro.disponibile:
                libro.disponibile = False
                return "Libro disponibile"
            return "Libro già prestato"
        return "Libro non trovato"
    
    def restituisci_libro(self, titolo: str) -> str:
        libro: Libro = [libro for libro in self.catalogo if titolo == libro.titolo][0]
        if libro:
            if not libro.disponibile:
                libro.disponibile = True
                return "Libro restituito"
            return "Libro già disponibile"
        return "Libro non trovato"

    def mostra_libri_disponibili(self) -> list[str]:
        lista_libri: list[str] = [libro.titolo for libro in self.catalogo if libro.disponibile]
        return lista_libri if lista_libri else "Nessun libro disponibile"

if __name__ == "__main__":
    libreria: Biblioteca = Biblioteca()
    print(libreria.aggiungi_libro(Libro("1984","George Orwell")))
    print(libreria.aggiungi_libro(Libro("War and Peace","Leo Tolstoy")))
    print(libreria.aggiungi_libro(Libro("Waste Land","T.S Eliot")))
    print(libreria.aggiungi_libro(Libro("Time Machine","H.G Wells")))
    print(libreria.presta_libro("War and Peace"))
    print(libreria.presta_libro("War and Peace"))
    print(libreria.restituisci_libro("War and Peace"))
    print(libreria.mostra_libri_disponibili())
