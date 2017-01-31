import string
import random

from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib import messages

from .models import Url


def index(request):
    '''Main view that enables creation of TinyUrl's'''
    tiny_url = request.session.pop('tiny_url', None)
    return render(request, 'index/index.html', {'tiny_url': tiny_url})


def generate(request):
    if not request.POST['destination_url']:
        messages.error(request, "Please specify a destination_url.")
        return redirect('index:index')

    def rand_tiny_url():
        length = random.choice(range(3, 8))
        symbols = (string.ascii_uppercase + string.digits)
        tiny_url = ''.join(random.choice(symbols) for _ in range(length))
        return tiny_url
    tiny_url = rand_tiny_url()
    while True:
        # TODO: this should be refactored to provide fixed generation time
        # for each request, e.g. use predefined list of available urls or
        # pre-generate few urls.
        if not Url.objects.filter(tiny_url=tiny_url).exists():
            break
        tiny_url = rand_tiny_url()

    url = Url(destination_url=request.POST['destination_url'],
              tiny_url=tiny_url,
              pub_date=timezone.now())
    url.save()
    request.session['tiny_url'] = url.tiny_url
    return redirect('index:index')


def redirection(request, tiny_url):
    '''View redirecting from tiny_url to destination_url'''
    url = get_object_or_404(Url, tiny_url=tiny_url)
    url.visit_counter += 1
    url.save()
    return redirect(url.destination_url)


def detail(request, tiny_url):
    '''Detail view of the tiny_url presenting stats'''
    url = get_object_or_404(Url, tiny_url=tiny_url)
    return render(request, 'index/detail.html', {'url': url})
