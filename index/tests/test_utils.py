from django.test import TestCase
from django.conf import settings

from index.utils import rand_tiny_url

RANDOM_ITERATION_LOOPS = 200


class RandTinyUrlTest(TestCase):

    def test_result_fixed_within_length_bounds(self):
        for _ in range(RANDOM_ITERATION_LOOPS):
            result = rand_tiny_url()
            bounds = settings.TINY_URL_LENGTH_BOUNDS
            assert bounds[0] <= len(result) <= bounds[1]
