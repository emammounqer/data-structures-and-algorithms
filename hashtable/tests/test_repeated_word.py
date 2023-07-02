from hashtable.repeated_word import repeated_word


def test_repeated_word():
    paragraph = "Once upon a time, there was a brave princess who..."
    assert repeated_word(paragraph) == 'a'

    paragraph = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."
    assert repeated_word(paragraph) == 'it'

    paragraph = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    assert repeated_word(paragraph) == 'summer'


def test_repeated_word_empty():
    paragraph = ""
    assert repeated_word(paragraph) == None
