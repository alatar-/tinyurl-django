from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import Url, User
import index.utils as utils


def index(request):
    '''Main view that enables creation of TinyUrl's'''
    urls = request.session.get('urls')
    return render(request, 'index/index.html', {'urls': urls})


def generate(request):
    if 'destination_url' not in request.POST:
        messages.error(request, "Please specify an URL.")
        return redirect('index:index')

    try:
        destination_url = utils.process_url(request.POST['destination_url'])
    except ValidationError:
        messages.error(request, "Destination URL is malformed. Please provide correct URL.")
        return redirect('index:index')
    else:
        url = Url.objects.filter(destination_url=destination_url).first()
        if not url:
            user = User.objects.random()
            url = user.url_set.create(
                destination_url=destination_url,
                tiny_url=utils.rand_tiny_url(),
                pub_date=timezone.now()
            )

        # Save at the beginning of session object
        session = request.session.get('urls', [])
        session.insert(0, url.tiny_url)
        request.session['urls'] = session

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
