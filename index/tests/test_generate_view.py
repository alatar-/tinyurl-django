from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.test.utils import setup_test_environment

from index.models import Url


def insert_url(destination_url, tiny_url):
    return Url.objects.create(
        destination_url=destination_url,
        tiny_url=tiny_url,
        pub_date=timezone.now()
    )


class GenerateViewTests(TestCase):
    fixture_destination_url = 'https://www.demo.com'
    destination_url_fixture_1 = 'demo.com.pl/asdfg?agda=5'
    destination_url_fixture_2 = 'https://demo.com'
    destination_url_fixture_1 = 'demo.com.'

    def test_correct_redirection_to_index_view(self):
        response = self.client.post(
            reverse('index:generate'),
            {'destination_url': self.fixture_destination_url}
        )
        self.assertRedirects(response, reverse('index:index'), status_code=302, target_status_code=200)

    def test_new_url_is_inserted_into_db(self):
        self.client.post(
            reverse('index:generate'),
            {'destination_url': self.fixture_destination_url}
        )
        assert len(Url.objects.all()) == 1
        assert len(Url.objects.filter(destination_url=self.fixture_destination_url)) == 1

    def test_new_url_is_passed_to_index_view(self):
        pass

    def test_pass_error_message_on_empty_post_body(self):
        setup_test_environment()
        response = self.client.post(
            reverse('index:generate'),
            {}
        )
        messages = list(response.context['messages'])
        assert len(messages) == 1
        assert messages[0] == 'Please specify a destination_url.'
