from django.test import TestCase

from index.utils import rand_tiny_url
from index.settings import TINY_URL_LENGTH_BOUNDS

RANDOM_ITERATION_LOOPS = 200


class RandTinyUrlTest(TestCase):

    def test_result_fixed_within_length_bounds(self):
        for _ in range(RANDOM_ITERATION_LOOPS):
            result = rand_tiny_url()
            assert TINY_URL_LENGTH_BOUNDS[0] <= len(result) <= TINY_URL_LENGTH_BOUNDS[1]
