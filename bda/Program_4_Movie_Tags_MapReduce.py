'''Develop a MapReduce program to find the tags associated with each movie by analyzing 
movie lens data.'''

import csv
import os

def create_sample_files():
    movies_data = [
        ['movieId', 'title'],
        ['1', 'Toy Story'],
        ['2', 'Jumanji'],
        ['3', 'Grumpier Old Men']
    ]

    tags_data = [
        ['userId', 'movieId', 'tag', 'timestamp'],
        ['10', '1', 'funny', '1234567890'],
        ['11', '1', 'animation', '1234567891'],
        ['12', '2', 'adventure', '1234567892'],
        ['13', '2', 'game', '1234567893'],
        ['14', '1', 'funny', '1234567894'],
        ['15', '3', 'romantic', '1234567895']
    ]

    with open('movies.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(movies_data)

    with open('tags.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tags_data)


def mapper(tags):
    key_value_pairs = []

    for row in tags:
        movie_id = row['movieId']
        tag = row['tag']
        key_value_pairs.append((movie_id, tag))

    return key_value_pairs


def reducer(key, values):
    return list(set(values))


def map_reduce(tags):
    key_value_pairs = mapper(tags)

    grouped_values = {}

    for key, value in key_value_pairs:
        if key not in grouped_values:
            grouped_values[key] = []

        grouped_values[key].append(value)

    result = {}

    for key in grouped_values:
        result[key] = reducer(key, grouped_values[key])

    return result


def load_tags(file_path):
    tags = []

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            tags.append(row)

    return tags


def load_movies(file_path):
    movies = {}

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            movies[row['movieId']] = row['title']

    return movies


create_sample_files()

tags = load_tags('tags.csv')
movies = load_movies('movies.csv')

result = map_reduce(tags)

for movie_id, tags in result.items():
    movie_title = movies.get(movie_id, "Unknown Title")
    print(f'Movie: {movie_title}, Tags: {", ".join(tags)}')