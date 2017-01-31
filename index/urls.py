from django.conf.urls import url
from . import views

app_name = 'index'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tiny_url>[A-z0-9]{3,9})/?$', views.redirection, name='redirection'),
    url(r'^!(?P<tiny_url>[A-z0-9]{3,9})/?$', views.detail, name='detail'),
]
