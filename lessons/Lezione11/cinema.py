# Gioele Amendola
# 29/05/2025

# Catalogo Film 
# Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere,
# rimuovere e cercare film di un particolare regista.
# Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

class MovieCatalog:

    def __init__(self) -> None:
        self.catalog: dict[str:list] = {}
    
    def add_movie(self, director_name: str, movies: list[str]|str) -> None:
        director_name = director_name.lower()
        if isinstance(movies, str):
            movies = [movies.lower()]
        if director_name in self.catalog:
            self.catalog[director_name] += [movie.lower() for movie in movies]
        else:
            self.catalog[director_name] = [movie.lower() for movie in movies]
    
    def remove_movie(self, director_name: str, movie_name: str) -> None:
        director_name = director_name.lower()
        movie_name = movie_name.lower()
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)
        if not self.catalog[director_name]:
            del self.catalog[director_name]

    def list_directors(self) -> None:
        print()
        for director in self.catalog:
            print("director: "+director)
        print()
    
    def get_movies_by_director(self, director_name: str) -> list[str]:
        director_name = director_name.lower()
        if director_name in self.catalog:
            return self.catalog[director_name]
    
    def search_movies_by_title(self, title: str) -> list[str]:
        result: list = []
        title = title.lower()
        for director in self.catalog:
            movies: list[str] = self.catalog[director]
            for movie in movies:
                if title in movie:
                    if director not in result:
                        result.append(director)
                    result.append(movie)
        if result:
            return result
        return f"No movie title with {title} in it was found"
                    
        

#     - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.

if __name__ == "__main__":
    catalog: MovieCatalog = MovieCatalog()
    catalog.add_movie("Quentin Tarantino","Pulp Fiction")
    catalog.add_movie("Quentin Tarantino",["Inglorious Bastards","Kill Bill Vol.1"])
    catalog.add_movie("Quentin Tarantino",["Django Unchained","The Hateful Eight"])
    catalog.add_movie("Quentin Tarantino","Kill Bill Vol.2")
    catalog.add_movie("Quentin Tarantino","Kill Bill Vol.3")
    catalog.add_movie("Steven Spielberg",["Schindler's List","Lincoln","Save Private Ryan","West Side Story","The terminal"])
    catalog.add_movie("Christopher Nolan",["Inception","Oppenheimer"])
    catalog.list_directors()
    print(catalog.get_movies_by_director("Christopher Nolan"))
    catalog.remove_movie("Christopher Nolan","Inception")
    catalog.remove_movie("Christopher Nolan","Oppenheimer")
    catalog.list_directors()
    print(catalog.get_movies_by_director("Quentin Tarantino"))
    print(catalog.search_movies_by_title("The"))
