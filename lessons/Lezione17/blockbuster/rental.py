from movie import Movie
from movie_genre import *

class Rental:

    def __init__(self, movie_list: list) -> None:
        self.movie_list: list = movie_list
        self.rented_movie: dict[int:list] = {}
    
    def isAvailable(self, movie: Movie) -> bool:
        return True if movie in self.movie_list else False
    
    def rentAMovie(self, movie: Movie, clientID: int) -> None | str:
        if self.isAvailable(movie):
            self.movie_list.remove(movie)
            if self.rented_movie[clientID]:
                self.rented_movie[clientID].append(movie)
            else:
                self.rented_movie[clientID] = [movie]
        else:
            return f"Not possible to rent the movie {movie.getTitle()}"
    
    def giveBack(self, movie: Movie, clientID: int, days: int) -> None:
        for i,xmovie in enumerate(self.rented_movie[clientID]):
            if xmovie == movie:
                del self.rented_movie[clientID][i]
                self.movie_list.append(movie)
                break
        if not self.rented_movie[clientID]:
            del self.rented_movie[clientID]

        total: float = movie.calculateLateFine(days)
        return f"Client: {clientID}! Needs to pay a fine for {movie.getTitle()} of {total}€!"
    
    def printMovies(self) -> list:
        for movie in self.movie_list:
            print(f"{movie.getTitle()} - {movie.getGenre()}")
        return self.movie_list
    
    def printRentMovies(self, clientID: int) -> list:
        for movie in self.rented_movie[clientID]:
            print(f"{movie.getTitle()} - {movie.getGenre()}")
        return self.rented_movie[clientID]


