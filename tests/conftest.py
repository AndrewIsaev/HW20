import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name="director1")
    director_2 = Director(id=2, name="director2")
    director_3 = Director(id=3, name="director3")

    directors = {1: director_1, 2: director_2, 3: director_3}

    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.create = MagicMock(return_value=Director(id=4, name="director4"))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="genre1")
    genre_2 = Genre(id=2, name="genre2")
    genre_3 = Genre(id=3, name="genre3")

    genres = {1: genre_1, 2: genre_2, 3: genre_3}

    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.create = MagicMock(return_value=Genre(id=4, name="genre4"))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao
