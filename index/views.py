from django.shortcuts import get_object_or_404, render
from .models import Url


def index(request):
    context = {'created_url': False}
    return render(request, 'index/index.html', context)


def detail(request, tiny_url):
    get_object_or_404(Url, tiny_url=tiny_url)
    return render(request, 'index/detail.html', {'url': tiny_url})
