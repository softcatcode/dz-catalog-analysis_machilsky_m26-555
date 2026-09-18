# 🎬 Анализ каталога фильмов (Catalog Analysis)

Данный проект представляет собой решение задачи по анализу каталога фильмов на Python. В рамках выполнения задания реализованы 9 этапов, демонстрирующих работу с базовыми типами данных, условиями, циклами, строками, коллекциями (списки, словари, множества), а также итераторами и генераторами.

## 🚀 Запуск проекта

Для работы с проектом требуется менеджер пакетов `uv` и Python 3.12.

1. Клонируйте репозиторий:
   ```bash
   git clone <url-вашего-репозитория>
   cd dz-catalog-analysis_machilsky_m26-555
   ```
2. Синхронизируйте виртуальное окружение и зависимости:
   ```bash
   uv sync
   ```
3. Запустите основной скрипт:
   ```bash
   uv run catalog_analysis.py
   ```
4. Проверка качества кода (линтер `ruff`):
   ```bash
   uv run ruff check catalog_analysis.py
   ```

---

## 📥 Исходные данные

В начало файла `catalog_analysis.py` добавлен следующий список словарей (часть заголовков намеренно записана не в Title Case):

```python
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
```

---

## 📋 Этапы выполнения

### Этап 1. Разминка: переменные, числа, `math`
#### 📌 Задача
Написать три функции для базовой статистики каталога:
1. `average_rating(movies)` — возвращает среднюю оценку, округленную до 1 знака (`round`).
2. `catalog_age_stats(movies, current_year=2026)` — возвращает кортеж `(самый старый фильм в годах, самый новый фильм в годах, среднее)`, где среднее округлено вверх (`math.ceil`).
3. `duration_in_hours(minutes)` — переводит минуты в формат `"2ч 35м"`, используя целочисленное деление и остаток.

#### ⚠️ Требования
- Использовать модуль `math` там, где это уместно.
- Применять `round()`, `//` и `%` по назначению.
- Результат `catalog_age_stats` должен быть неизменяемым (`tuple`).

---

### Этап 2. Условия и `match`
#### 📌 Задача
1. `rating_tier(rating)` — возвращает категорию: "шедевр" (≥9), "хорошо" (7–8.9), "средне" (5–6.9), "слабо" (<5).
2. `decade_label(year)` — возвращает метку "новые" (после 2020), "недавние" (2015–2020) или "старые" (раньше 2015).

#### ⚠️ Требования
- `rating_tier` обязательно реализуется через `if/elif`, внутри должен быть использован хотя бы один тернарный оператор.
- `decade_label` обязательно реализуется через `match` с использованием `case _ if ...` для сопоставления диапазонов.
- Границы диапазонов не должны пересекаться и терять пограничные значения.

---

### Этап 3. Циклы
#### 📌 Задача
Продемонстрировать работу с `for`, `while` и управляющими конструкциями:
1. С помощью `for` и `continue` вывести названия фильмов, которые **НЕ** относятся к жанру "comedy".
2. С помощью `while` и `break` найти первый фильм с рейтингом > 9.0. Если такого нет, цикл должен завершиться веткой `else` с сообщением "Шедевров не найдено".
3. `count_long_movies(movies, threshold=120)` — считает количество фильмов длиннее `threshold` минут через `for` с накопительной переменной.

#### ⚠️ Требования
- Обязательно использовать `continue` и `break`.
- Ветка `else` цикла `while` должна быть задействована.
- В `count_long_movies` нельзя использовать `sum()` по списку-фильтру.

---

### Этап 4. Строки
#### 📌 Задача
1. `normalize_title(title)` — приводит строку к Title Case без использования `str.title()` (разбить по пробелам, собрать вручную через срез `word[0].upper() + word[1:]`).
2. `make_slug(title)` — превращает название в слаг вида `the-quiet-algorithm`.
3. `format_report_line(movie)` — возвращает единую строку с описанием фильма.

#### 📊 Пример результата
```python
normalize_title("silent hours")      # "Silent Hours"
make_slug("Silent Hours")            # "silent-hours"
format_report_line(movies[7])
# '"The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi'
```

#### ⚠️ Требования
- `normalize_title` без `str.title()`.
- `make_slug` использует `.lower()` и `.replace()`.
- `format_report_line` собирается через f-строку, вызывает `duration_in_hours`, жанры отсортированы по алфавиту.

---

### Этап 5. Списки
#### 📌 Задача
1. `titles_sorted_by_rating(movies)` — возвращает список названий, отсортированных по убыванию рейтинга.
2. `top_n_by_rating(movies, n=3)` — возвращает список из `n` кортежей `(title, rating)`.

#### ⚠️ Требования
- Сортировка через `sorted()` с параметром `key`, а не вручную.
- Каждая запись в `top_n_by_rating` — именно `tuple`.
- Исходный список `movies` не должен изменяться.

---

### Этап 6. Словари
#### 📌 Задача
1. `count_by_genre(movies)` — возвращает словарь `{жанр: количество}`, построенный вручную через цикл и `dict.get()`.
2. `actor_filmography(movies)` — возвращает словарь `{актер: [список названий фильмов]}`.
3. С помощью генератора словаря (dict comprehension) построить словарь `{title: rating}` только для фильмов с рейтингом выше среднего.

#### ⚠️ Требования
- Не использовать `collections.Counter`.
- Получать значение по умолчанию через `dict.get(key, 0)`.
- Словарь выше среднего строится строго через dict comprehension.

---

### Этап 7. Множества
#### 📌 Задача
1. `all_genres(movies)` — возвращает множество всех уникальных жанров.
2. `common_actors(movie1, movie2)` — возвращает множество актеров, снимавшихся в обоих фильмах.
3. `genres_only_in_one(movies_a, movies_b)` — возвращает жанры, встречающиеся в `movies_a`, но не в `movies_b`.

#### ⚠️ Требования
- `all_genres` строится через объединение (`|` или `.update()`).
- `common_actors` использует пересечение (`&`).
- `genres_only_in_one` использует разность (`-`).

---

### Этап 8. Итераторы и генераторы
#### 📌 Задача
1. `iter_high_rated(movies, min_rating=8.0)` — функция-генератор, которая через `yield` лениво отдает фильмы с рейтингом не ниже `min_rating`.
2. Продемонстрировать работу циклом `for` с вызовом `format_report_line`.
3. Написать генераторное выражение для подсчета суммарной длительности фильмов с рейтингом > 7, переданное в `sum()`.

#### 📊 Пример результата
```python
sum(m["duration_min"] for m in movies if m["rating"] > 7)   # 713
```

#### ⚠️ Требования
- Использовать `yield`, а не возврат готового списка.
- Суммирование через генераторное выражение внутри `sum()` (без квадратных скобок `[]`).

---

### Этап 9. Итоговый отчет
#### 📌 Задача
Написать функцию `build_report(movies)`, которая объединяет результаты всех этапов в единый консольный отчет.

#### 📊 Пример отчета
```text
ОТЧЁТ ПО КАТАЛОГУ
Средний рейтинг: 7.2
Средний возраст фильмов: 8 лет

Топ-3 фильма:
  "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi
  "Midnight In Oslo" (2020) — 8.9/10, 2ч 4м, жанры: mystery, thriller
  "The Dune Chronicles" (2021) — 8.6/10, 2ч 35м, жанры: drama, sci-fi

Фильмов по жанрам:
  drama — 5
  comedy — 3
  sci-fi — 3
  thriller — 3
  action — 2
  mystery — 1

Все жанры каталога: action, comedy, drama, mystery, sci-fi, thriller
```

#### ⚠️ Требования
- `build_report` — единственная точка входа (один вызов воспроизводит весь отчет).
- Жанры в списке количества отсортированы по убыванию числа фильмов.
- Полный список жанров выводится одной строкой через `", ".join(...)`.

---

## 🛠️ Технологии
- **Python 3.12**
- **uv** (управление проектом и зависимостями)
- **ruff** (линтинг и форматирование кода)
- Стандартная библиотека Python (`math`, `typing`)
