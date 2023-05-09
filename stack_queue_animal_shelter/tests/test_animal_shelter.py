from stack_queue_animal_shelter.animal import Cat, Dog
from stack_queue_animal_shelter.animal_shelter import AnimalShelter


def test_enqueue_cat():
    shelter = AnimalShelter()
    new_cat = Cat('new cat')
    shelter.enqueue(new_cat)

    assert shelter.cats.peek() == new_cat
    assert shelter.dogs.is_empty()


def test_enqueue_dog():
    shelter = AnimalShelter()
    new_dog = Dog('new dog')
    shelter.enqueue(new_dog)

    assert shelter.dogs.peek() == new_dog
    assert shelter.cats.is_empty()


def test_enqueue_cat_and_dog():
    shelter = AnimalShelter()
    new_cat = Cat('new cat')
    new_dog = Dog('new dog')
    shelter.enqueue(new_cat)
    shelter.enqueue(new_dog)

    assert shelter.cats.peek() == new_cat
    assert shelter.dogs.peek() == new_dog


def test_dequeue_cat():
    shelter = AnimalShelter()
    new_cat = Cat('new cat')
    shelter.enqueue(new_cat)

    assert shelter.dequeue('cat') == new_cat
    assert shelter.cats.is_empty()


def test_dequeue_dog():
    shelter = AnimalShelter()
    new_dog = Dog('new dog')
    shelter.enqueue(new_dog)

    assert shelter.dequeue('dog') == new_dog
    assert shelter.cats.is_empty()


def test_dequeue_cat_and_dog():
    shelter = AnimalShelter()
    new_cat = Cat('new cat')
    new_dog = Dog('new dog')
    shelter.enqueue(new_cat)
    shelter.enqueue(new_dog)

    assert shelter.dequeue('cat') == new_cat
    assert shelter.dequeue('dog') == new_dog
    assert shelter.cats.is_empty()
    assert shelter.dogs.is_empty()


def test_dequeue_cat_when_it_is_empty():
    shelter = AnimalShelter()

    assert shelter.dequeue('cat') == None
    assert shelter.cats.is_empty()


def test_dequeue_dog_when_it_is_empty():
    shelter = AnimalShelter()

    assert shelter.dequeue('dog') == None
    assert shelter.dogs.is_empty()


def test_dequeue_any():
    shelter = AnimalShelter()
    new_cat = Cat('new cat')
    new_dog = Dog('new dog')
    shelter.enqueue(new_cat)
    shelter.enqueue(new_dog)

    assert shelter.dequeue("any") == None
    assert shelter.dequeue("other") == None
