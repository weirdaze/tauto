from django.conf.urls import url, include
from . import views

app_name = 'account'

urlpatterns = [
    # /account/
    url(r'^$', views.index, name='index'),
    url(r'^sample/$', views.sample, name='sample'),
]