import random

from .models import Url
import index.settings as cfg


def rand_tiny_url():
    def get_url():
        length = random.choice(range(*cfg.TINY_URL_LENGTH_BOUNDS))
        return ''.join(random.choice(cfg.TINY_URL_SYMBOLS) for _ in range(length))

    while True:
        # TODO: should be refactored to provide fixed generation time
        # for each request, e.g. use predefined list of available urls
        # or schedule pre-generation.
        url = get_url()
        if not Url.objects.filter(tiny_url=url).exists():
            return url
