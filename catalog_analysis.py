import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    """Средний рейтинг"""
    if not movies:
        return 0.0
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)

def catalog_age_stats(movies, current=2026):
    """Возраст фильмов (самый старый, самый новый, средний возраст)"""
    if not movies:
        return (0, 0, 0)
    ages = [current - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

def no_comedi(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def first_shedevr(movies):
    i = 0
    while i < len(movies):
        movie = movies[i]
        if movie["rating"] > 9.0:
            print(movie["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    c = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            c += 1
    return c

def normalize_title(title):
    return " ".join(word[0].upper() + word[1:] for word in title.split())


def make_slug(title):
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f"{movie['rating']}/10, {duration_in_hours(movie['duration_min'])}, "
        f"жанры: {genres}"
    )

def titles_sorted_by_rating(movies):
    s = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in s]

def top_n_by_rating(movies, n=3):
    s = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in s[: max(0, n)]]

def count_by_genre(movies):
    c = {}
    for movie in movies:
        for genre in movie["genres"]:
            c[genre] = c.get(genre, 0) + 1
    return c


def actor_filmography(movies):
    f = {}
    for movie in movies:
        for actor in movie["actors"]:
            t = f.get(actor, [])
            t.append(movie["title"])
            f[actor] = t
    return f


def ratings_above_average(movies):
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average
    }

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def high_rated(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def total_duration(movies, rating_threshold=7):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > rating_threshold)

def build_report(movies):
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print("Средний рейтинг:", average_rating(movies))
    oldest, newest, average = catalog_age_stats(movies)
    print(f"Самый старый фильм: {oldest} лет")
    print(f"Самый новый фильм: {newest} лет")
    print(f"Средний возраст фильмов: {average} лет")
    for movie in movies:
        print(f" - {movie['title']} ({movie['year']}): {duration_in_hours(movie['duration_min'])}")

    print("\nРейтинги фильмов:")
    for movie in movies:
        print(f" - {movie['title']}: {rating_tier(movie['rating'])}")
    print("\nДесятилетия фильмов:")
    for movie in movies:
        print(f" - {movie['title']}: {decade_label(movie['year'])}")

    print("\nФильмы не относящиеся к комедиям:")
    no_comedi(movies)
    print("\nПервый шедевр в каталоге:")
    first_shedevr(movies)
    print("\nКоличество фильмов длиннее 120 минут:", count_long_movies(movies))

    print("\nНормализованные названия фильмов:\n")
    for movie in movies:
        print(normalize_title(movie["title"]))
    print("\nСлоги фильмов:")
    for movie in movies:
        print(make_slug(movie["title"]))
    print("Отформатированные строки отчета:")
    for movie in movies:
        print(format_report_line(movie))

    print("\nНазвания фильмов, отсортированные по рейтингу:")
    for title in titles_sorted_by_rating(movies):
        print(title)
    print("\nТоп 3 фильма по рейтингу:")
    for title, rating in top_n_by_rating(movies):
        print(f"{title}: {rating}")

    print("\nКоличество фильмов по жанрам:")
    for g, c in count_by_genre(movies).items():
        print(f"{g}: {c}")

    print("\nФильмография актеров:")
    for a, f in actor_filmography(movies).items():
        print(f"{a}: {', '.join(f)}")

    print("\nРейтинги выше среднего:")
    for t, r in ratings_above_average(movies).items():
        print(f"{t}: {r}")

    print("\nВсе жанры в каталоге:")
    print(", ".join(sorted(all_genres(movies))))
    print("\nОбщие актеры между фильмами:")
    print(common_actors(movies[0], movies[3]))
    print("\nЖанры, которые есть только в одном из каталогов:")
    print(genres_only_in_one(movies[5:6], movies[:5]))

    print("\nФильмы с высоким рейтингом:")
    high_rated(movies)
    print("\nОбщая продолжительность фильмов с рейтингом выше 7:", total_duration(movies))

if __name__ == "__main__":
    build_report(movies)