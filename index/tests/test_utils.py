from index.utils import rand_tiny_url
from index.settings import SHORT_URL_LENGTH_BOUNDS

RANDOM_ITERATION_LOOPS = 200


class RandTinyUrlTest:

    def test_result_fixed_within_length_bounds(self):
        for _ in range(RANDOM_ITERATION_LOOPS):
            result = rand_tiny_url()
            assert SHORT_URL_LENGTH_BOUNDS[0] <= len(result) <= SHORT_URL_LENGTH_BOUNDS[1]

# class ParseDestinationUrlTest:
#     destination_url_fixture_1 = 'demo.com.pl/asdfg?agda=5'
#     destination_url_fixture_2 = 'https://demo.com'
#     destination_url_fixture_1 = 'demo.com.'
