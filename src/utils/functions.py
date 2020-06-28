import string
import random


def random_string(string_length=8):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(string_length))


def filter_response():
    pass
