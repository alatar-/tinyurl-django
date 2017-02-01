from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib import messages

from .models import Url, User
from .utils import rand_tiny_url


def index(request):
    '''Main view that enables creation of TinyUrl's'''
    tiny_url = request.session.pop('tiny_url', None)
    return render(request, 'index/index.html', {'tiny_url': tiny_url})


def generate(request):
    if 'destination_url' not in request.POST:
        messages.error(request, "Please specify a destination_url.")
        return redirect('index:index')

    user = User.objects.random()
    url = user.url_set.create(
        destination_url=request.POST['destination_url'],
        tiny_url=rand_tiny_url(),
        pub_date=timezone.now()
    )
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
