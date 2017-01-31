from django.shortcuts import get_object_or_404, render, redirect
from .models import Url


def index(request):
    '''Main view that enables creation of TinyUrl's'''
    context = {'created_url': False}
    return render(request, 'index/index.html', context)


def redirection(request, tiny_url):
    '''View redirecting from tiny_url to destination_url'''
    url = get_object_or_404(Url, tiny_url=tiny_url)
    return redirect(url.destination_url)


def detail(request, tiny_url):
    '''Detail view of the tiny_url presenting stats'''
    url = get_object_or_404(Url, tiny_url=tiny_url)
    return render(request, 'index/detail.html', {'url': url})
