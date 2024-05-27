# Gioele Amendola
# 24/05/2024

class Movie:

    def __init__(self, title: str, duration: int) -> None:
        self.title: str = title
        self.duration: int = duration

class Room:

    def __init__(self, id: str, movies: list[Movie], total_seats: int, taken_seats: int = 0) -> None:
        self.id: str = id
        self.movies: dict[Movie:list] = {movie: [movie.title, taken_seats] for movie in movies}
        self.total_seats: int = total_seats
    
    def book_seats(self, seats: int, name: Movie = None) -> None:
        if not name:
            name = list(self.movies.keys())[0]
        if self.total_seats - self.movies[name][1] - seats >= 0:
            self.movies[name][1] += seats
            print(f"{seats} seats booked for {self.movies[name][0]}.")
        else:
            print(f"There aren't enough seats available for {self.movies[name][0]} to book {seats} seats. Remaining: {self.total_seats-self.movies[name][1]}")
    
    def available_seats(self, name: Movie = None) -> int:
        if not name:
            name = list(self.movies.keys())[0]
        return self.total_seats - self.movies[name][1]
    
    def __str__(self) -> str:
        string: str = f"\nRoom number: {self.id}\nMovies:\n"
        for movie in self.movies:
            string += f"\nName: {movie.title}\nAvailable seats: {self.total_seats-self.movies[movie][1]}\n"
            string += f"Duration: {movie.duration} minutes\n{'-'*22}"
        return string


class Cinema:

    def __init__(self, rooms: list[Room] = []) -> None:
        self.rooms: list[Room] = rooms
    
    def add_room(self, room: Room) -> None:
        self.rooms.append(room)
    
    def book_movie(self, movie_name: str, seats: int) -> None:
        # creates list of movies
        movies_list: list[Movie] = [room.movies for room in self.rooms]
        # creates a dictionary with key being the str(list of movies) and value being the room
        movies_room: dict = {str(room.movies): room  for room in self.rooms}
        # takes list of movies from room
        for movies in movies_list:
            # takes movie from the list
            for movie in movies:
                # check movie title with the one given
                if movie.title == movie_name:
                    # if found get value from the dictionary
                    movies_room[str(movies)].book_seats(seats, movie)
                    return
        # not found movie with that name
        print(f"There is no movie called {movie_name} in this cinema")

if __name__ == "__main__":
    # Creation of theater
    theater: Cinema = Cinema()
    # No movie with that name
    theater.book_movie("alimo",13)
    # Add room with movies "alimo" and "priscilla" with 10 seats available
    theater.add_room(Room("37",[Movie("alimo",90),Movie("Priscilla",45),Movie("I am legend",60),Movie("KungFu Panda 4",120)],10))
    # Cannot book (10 available)
    theater.book_movie("alimo",13)
    # Book successful
    theater.book_movie("Priscilla",5)
    theater.book_movie("alimo",7)
    theater.book_movie("I am legend",10)
    theater.book_movie("KungFu Panda 4",3)
    # available seats
    print(theater.rooms[-1].movies[list(theater.rooms[-1].movies.keys())[0]][0],end=": ")
    print(theater.rooms[-1].available_seats())
    print(theater.rooms[-1].movies[list(theater.rooms[-1].movies.keys())[1]][0],end=": ")
    print(theater.rooms[-1].available_seats(list(theater.rooms[-1].movies.keys())[1]))
    for room in theater.rooms:
        print(str(room))