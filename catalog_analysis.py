from math import ceil
from typing import Dict, Iterator, List

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"]
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"]
    },
    {
        "title": "Comet Racers",
        "year": 2023, 
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"]
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"]
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"]
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"]
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"]
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"]
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"]
    },
]


def average_rating(
    movies: List[Dict[str, int | str | List[str]]]
) -> float:
    ratings = [item["rating"] for item in movies]
    result = sum(ratings) / len(ratings) if len(ratings) > 0 else 0
    return round(result, 1)

def duration_in_hours(minutes: int) -> str:
    return f'{minutes // 60}ч {minutes % 60}м'

def catalog_age_stats(
    movies: List[Dict[str, int | str | List[str]]],
    current_year: int = 2026
) -> tuple[int, int, int]:
    
    age = [current_year - item["year"] for item in movies]
    average = ceil(sum(age) / len(age))
    return max(age), min(age), average

def rating_tier(rating: float) -> str:
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо" if rating < 5 else "ошибка"

def decade_label(year: int) -> str:
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

def count_long_movies(
    movies: List[Dict[str, int | str | List[str]]],
    threshold: int = 120
):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

def task3() -> None:
    print("Фильмы, которые не относятся к жанру comedy:")
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(f"  - {movie['title']}")
    
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            print(f"\nШедевр: {movie['title']}")
            break
        index += 1
    else:
        print("\nШедевров не найдено")   
    
    long_movies_count = count_long_movies(movies)
    print(f"\nКоличество фильмов длиннее 120 минут: {long_movies_count}")

def normalize_title(title: str) -> str:
    words = title.split()
    words = [w[0].upper() + w[1:] for w in words]
    return ' '.join(words)

def make_slug(title: str) -> str:
    return title.lower().replace(' ', '-')

def format_report_line(
    movie: Dict[str, int | str | List[str]]
) -> str:
    genre_names = ', '.join(sorted([w for w in movie['genres']]))
    duration = duration_in_hours(movie['duration_min'])
    s = f'"{movie['title']}" ({movie['year']}) — {movie['rating']}/10'
    s += f', {duration}, жанры: {genre_names}'
    return s

def titles_sorted_by_rating(
    movies: List[Dict[str, int | str | List[str]]]
) -> List[str]:
    sorted_movies = sorted(movies, key=lambda x: x['rating'], reverse=True)
    return [elem['title'] for elem in sorted_movies]

def top_n_by_rating(
    movies: List[Dict[str, int | str | List[str]]],
    n: int = 3
) -> List[tuple[str, float]]:
    sorted_movies = sorted(movies, key=lambda x: x['rating'], reverse=True)
    sorted_movies = sorted_movies[ : min(len(sorted_movies), n)]
    answer = [(elem['title'], elem['rating']) for elem in sorted_movies]
    return answer

def count_by_genre(
    movies: List[Dict[str, int | str | List[str]]]
) -> Dict[str, int]:
    genre_counts = {}
    for movie in movies:
        for genre in movie['genres']:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts

def actor_filmography(
    movies: List[Dict[str, int | str | List[str]]]
) -> Dict[str, List[str]]:
    actor_films = {}
    for movie in movies:
        for actor in movie['actors']:
            actor_films[actor] = actor_films.get(actor, []) + [movie['title']]
    return actor_films

def task6() -> None:
    avg = average_rating(movies)
    answer = { \
        elem['title']: elem['rating'] \
        for elem in movies \
        if elem['rating'] > avg}
    print(answer)

def all_genres(
    movies: List[Dict[str, int | str | List[str]]]
) -> set[str]:
    answer = set()
    for movie in movies:
        answer.update(movie['genres'])
    return answer

def common_actors(
    movie1: Dict[str, int | str | List[str]],
    movie2: Dict[str, int | str | List[str]]
) -> set[str]:
    return set(movie1['actors']) & set(movie2['actors'])

def genres_only_in_one(
    movies_a: List[Dict[str, int | str | List[str]]],
    movies_b: List[Dict[str, int | str | List[str]]]
) -> set[str]:
    return all_genres(movies_a) - all_genres(movies_b)

def iter_high_rated(
    movies: List[Dict[str, int | str | List[str]]],
    min_rating: float = 8.0
) -> Iterator[dict]:
    for movie in movies:
        if movie['rating'] >= min_rating:
            yield movie

def task8() -> None:
    for movie in iter_high_rated(movies, 8.5):
        print(format_report_line(movie))
    longitude = sum( \
        movie['duration_min'] \
        for movie in movies if movie['rating'] > 7)
    print(longitude)

def build_report(
    movies: List[Dict[str, int | str | List[str]]]
) -> None:
    print('ОТЧЁТ ПО КАТАЛОГУ')
    print('Средний рейтинг:', average_rating(movies))
    print('Средний возраст фильмов:', catalog_age_stats(movies)[2], 'лет')
    
    print('\nТоп-3 фильма:')
    top_movies = top_n_by_rating(movies, 3)
    for title, _ in top_movies:
        movie_obj = next(m for m in movies if m['title'] == title)
        print(f'  {format_report_line(movie_obj)}')
    
    print('\nФильмов по жанрам:')
    genres = sorted(
        count_by_genre(movies).items(),
        key = lambda x: x[1],
        reverse=True
    )
    for elem in genres:
        print(f'  {elem[0]} — {elem[1]}')
    
    print('\nВсе жанры каталога:', end=' ')
    print(', '.join(sorted(all_genres(movies))), end='\n\n')
    
    print('Задание 3')
    task3()
    print()
    
    print('Задание 6')
    task6()
    print()
    
    print('Задание 8')
    task8()
    print()

build_report(movies)