"""Seeding database"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later

movies_in_db = []

for movie in movie_data:

    format1 = "%Y-%m-%d"

    mov_title = movie['title']
    mov_overview = movie['overview']
    mov_poster_path = movie['poster_path']
    mov_release_date = datetime.strptime(movie['release_date'], format1)

    new_movie = crud.create_movie(mov_title, mov_overview, mov_release_date, mov_poster_path)

    movies_in_db.append(new_movie)


for n in range(10):

    email = f'user{n}@test.com'
    password = 'test'

    new_user = crud.create_user(email, password)

    for i in range (10):

        current_movie = choice(movies_in_db)
        current_score = randint(1,5)

        new_rating = crud.create_rating(new_user, current_movie, current_score)
