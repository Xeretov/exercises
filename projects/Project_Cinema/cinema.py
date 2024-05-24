# Gioele Amendola
# 24/05/2024

class Movie:

    def __init__(self, title: str, duration: int) -> None:
        self.title: str = title
        self.duration: int = duration

class Room:

    def __init__(self, id: str, movies: list[Movie], total_seats: int, taken_seats: int = 0) -> None:
        self.id: str = id
        self.movies: list[Movie] = movies
        self.total_seats: int = total_seats
        self.taken_seats: int = taken_seats
    
    def book_seats(self, seats: int) -> None:
        if self.total_seats - self.taken_seats - seats >= 0:
            self.taken_seats += seats
            print("Seats booked.")
        else:
            print(f"There aren't enough seats available {self.total_seats-self.taken_seats} to book {seats}")
    
    def available_seats(self) -> int:
        return self.total_seats - self.taken_seats

class Cinema:

    def __init__(self, rooms: list[Room] = []) -> None:
        self.rooms: list[Room] = rooms
    
    def add_room(self, room: Room) -> None:
        self.rooms.append(room)
    
    def book_movie(self, movie_name: str, seats) -> None:
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
                    movies_room[str(movies)].book_seats(seats)
                    return
        # not found movie with that name
        print(f"There is no movie called {movie_name} in this cinema")

if __name__ == "__main__":
    # Creation of movie list
    # movies = [movie("1",180),movie("2",180)...]
    movies: list[Movie] = [Movie(str(title),180) for title in range(1,11)]
    # Creation of rooms list
    # rooms = [Room("0", [movie("1",180),movie("2",180)], 20), Room("1", [movie("2",180),movie("3",180)], 20)]
    rooms: list[Room] = [Room(str(index),[movies[index],movies[index+1]],20) for index in range(len(movies)-1)]
    # Creation of theater
    theater: Cinema = Cinema()
    for room in rooms:
        # Adds rooms to theater
        theater.add_room(room)
    # Returns 20
    print(rooms[0].available_seats())
    # Book successfull
    rooms[0].book_seats(13)
    # Cannot book (7 available)
    rooms[0].book_seats(8)
    # Book successfull
    theater.book_movie("1",3)
    # Cannot book (4 available)
    theater.book_movie("1",20)
    # No movie with that name
    theater.book_movie("alimo",13)
    # Add room with movies "alimo" and "priscilla" with 10 seats available
    theater.add_room(Room("37",[Movie("alimo",90),Movie("Priscilla",45)],10))
    # Cannot book (10 available)
    theater.book_movie("alimo",13)
    # Book successful
    theater.book_movie("Priscilla",5)
    # Book successful
    theater.book_movie("alimo",5)