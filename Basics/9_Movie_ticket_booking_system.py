class Movie:
    def __init__(self, name, st, seats):
        self.name, self.st, self.seats = name, st, seats
        self.booked = []
    def avs(self):
        return [s for s in self.seats if s not in self.booked]
    def book(self, seat):
        if seat in self.avs():
            self.booked.append(seat)
            return True
        return False
movies = {
    "1": Movie("Toxic", ["6am","11am","4pm"], ["A1","A2","A3"]),
    "2": Movie("KGF", ["6am","11am","4pm"], ["B1","B2","B3"])
}
while True:
    print("\nMovies:")
    for k,m in movies.items(): 
        print(f"{k}. {m.name}")
    choice = input("Movie number: ")
    if choice=="q": break
    if choice not in movies: continue

    movie = movies[choice]
    print(f"Showtimes: {', '.join(movie.st)}")
    time = input("Choose showtime: ")
    if time not in movie.st: continue

    print(f"Available seats: {', '.join(movie.avs())}")
    seat = input("Choose seat: ")
    if movie.book(seat):
        print(f"Booked {seat} for {movie.name} at {time} ")
    else:
        print("Seat nahi hai bhai!")