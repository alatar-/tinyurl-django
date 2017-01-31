from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^!(?P<tiny_url>[A-z0-9]{3,9})/?$', views.detail, name='detail'),
]
