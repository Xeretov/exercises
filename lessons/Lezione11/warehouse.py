# Gioele Amendola
# 25/05/2024

# Scrivi un programma in Python che gestisca un magazzino. 
# Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità
# di un prodotto.

# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)
 
# Definisci una classe Magazzino con i seguenti metodi:
# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.

class Product:
    
    def __init__(self, name: str, quantity: int) -> None:
        self.name: str = name
        self.quantity: int = quantity
    
    def __str__(self) -> str:
        return f"{self.name} has {self.quantity} left."

class Warehouse:
    
    def __init__(self, products: list[Product] = []) -> None:
        self.products: list[Product] = products

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def search_product(self, name: str) -> Product | str:
        for product in self.products:
            if name == product.name:
                return product
        return f"Product {name} not found in warehouse."

    def is_available(self, name: str) -> str:
        for product in self.products:
            if name == product.name:
                if product.quantity > 0:
                    return f"The product {name} is available. Quantity remaining: {product.quantity}"
                else:
                    return f"The product {name} is currently unavailable."
        return f"Product {name} not found in warehouse."

if __name__ == "__main__":
    
    product1: Product = Product("Barilla", 20)
    product2: Product = Product("Lion", 0)
    warehouse1: Warehouse = Warehouse([product1])
    warehouse1.add_product(product2)
    print(str(warehouse1.search_product("Barilla")))
    print(warehouse1.search_product("gelato"))
    print(warehouse1.is_available("Barilla"))
    print(warehouse1.is_available("Lion"))