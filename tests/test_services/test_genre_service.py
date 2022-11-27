import pytest
from unittest.mock import MagicMock
from service.genre import GenreService

class TestGenreService():
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None
        assert len(genres)>0