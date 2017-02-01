import string
import random

from .settings import SHORT_URL_LENGTH_BOUNDS


def rand_tiny_url():
    length = random.choice(range(*SHORT_URL_LENGTH_BOUNDS))
    symbols = (string.ascii_uppercase + string.digits)
    tiny_url = ''.join(random.choice(symbols) for _ in range(length))
    return tiny_url
