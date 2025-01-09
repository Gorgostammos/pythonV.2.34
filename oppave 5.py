ok_movies = [
    {'name': 'Inception', 'year': 2010, 'rating': 8.7},
    {'name': 'Inside Out', 'year': 2015, 'rating': 8.1},
    {'name': 'Con Air', 'year': 1997, 'rating': 6.9}

]

best_movies = []


def add_movie(movie_list, name, year, rating=5):
    movie_list.append({'name': name, 'year': year, 'rating': rating})


add_movie(best_movies, "lord of the rings", 2001, 9)


# oppgave 5.2
def prin_movies(movie_list):
    for movie in movie_list:
        print(f"{movie['name']}- {movie['year']} has a rating of {movie['rating']}")


print()
prin_movies(ok_movies)


def avg_rating(movie_list):
    sum_rating = 0.0
    for movie in movie_list:
        sum_rating += movie['rating']
    return sum_rating / len(movie_list)


print(avg_rating(ok_movies))


def get_movies_after_year(movie_list, year):
    movies_after_year = []
    for movie in movie_list:
        if movie['year'] >= year:
            movies_after_year.append(movie)
    return movies_after_year


print(get_movies_after_year(ok_movies, 2000))


# oppgave 5.3
def write_movie(movie_list, filename):
    with open(filename, 'w') as movie_file:
        for movie in movie_list:
            movie_file.write(f"{movie['name']}\n")


def read_file(filename):
    file = open(filename, 'r')
    print(file.read())
    file.close()


write_movie(ok_movies, "ok_movies.txt")

read_file("ok_movies.txt")
