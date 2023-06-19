import pytest

from ..fun import sort_by_name, sort_by_year


@pytest.fixture
def movies():
    return [
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Drama", "Crime"]
        },
        {
            "title": "The Godfather",
            "year": 1972,
            "genres": ["Crime", "Drama"]
        },
        {
            "title": "The Godfather: Part II",
            "year": 1974,
            "genres": ["Crime", "Drama"]
        },
        {
            "title": "The Dark Knight",
            "year": 2008,
            "genres": ["Action", "Crime", "Drama", "Thriller"]
        },
        {
            "title": "pulp fiction",
            "year": 1994,
            "genres": ["Crime", "Drama"]
        },
    ]


def test_sort_by_name(movies):
    sorted_movies = sort_by_name(movies)
    assert sorted_movies[0]["title"] == "The Dark Knight"
    assert sorted_movies[1]["title"] == "The Godfather"
    assert sorted_movies[2]["title"] == "The Godfather: Part II"
    assert sorted_movies[3]["title"] == "pulp fiction"
    assert sorted_movies[4]["title"] == "The Shawshank Redemption"


def test_sort_by_year(movies):
    sorted_movies = sort_by_year(movies)
    assert sorted_movies[0]["year"] == 1972
    assert sorted_movies[1]["year"] == 1974
    assert sorted_movies[2]["year"] == 1994
    assert sorted_movies[3]["year"] == 1994
    assert sorted_movies[4]["year"] == 2008
