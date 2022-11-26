import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
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


