import re
from hashtable.hashtable import Hashtable


def repeated_word(paragraph: str):
    words: list[str] = re.findall(r'\w+', paragraph)

    hashtable = Hashtable()

    for word in words:
        if hashtable.has(word.lower()):
            return word
        hashtable.set(word.lower(), True)
