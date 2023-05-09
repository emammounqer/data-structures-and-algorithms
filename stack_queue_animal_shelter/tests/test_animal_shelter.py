import pytest
from stack_queue_animal_shelter.animal import Animal
from stack_queue_animal_shelter.animal_shelter import AnimalShelter


@pytest.fixture
def shelter():
    shelter = AnimalShelter()
    first_dog = Animal("dog", 'first dog')
    sec_dog = Animal("dog", 'sec dog')
    first_cat = Animal("cat", 'first cat')
    sec_cat = Animal("cat", 'sec cat')

    shelter.enqueue(first_dog)
    shelter.enqueue(first_cat)
    shelter.enqueue(sec_dog)
    shelter.enqueue(sec_cat)
    return shelter


def test_enqueue_one_animal():
    shelter = AnimalShelter()
    new_cat = Animal("cat", 'new cat')
    shelter.enqueue(new_cat)

    assert shelter.animals[0] == new_cat


def test_enqueue_multiple_animal(shelter: AnimalShelter):
    assert len(shelter.animals) == 4
    assert shelter.animals[0].name == "first dog"


def test_dequeue_one_animal(shelter: AnimalShelter):
    cat = shelter.dequeue('cat')
    assert cat is not None
    assert cat.name == "first cat"
    assert len(shelter.animals) == 3


def test_dequeue_all_animal(shelter: AnimalShelter):
    cat1 = shelter.dequeue('cat')
    cat2 = shelter.dequeue('cat')
    dog1 = shelter.dequeue('dog')
    dog2 = shelter.dequeue('dog')

    assert cat1 and cat1.name == "first cat"
    assert cat2 and cat2.name == "sec cat"
    assert dog1 and dog1.name == "first dog"
    assert dog2 and dog2.name == "sec dog"
    assert len(shelter.animals) == 0

    assert shelter.dequeue('cat') is None
    assert shelter.dequeue('dog') is None
