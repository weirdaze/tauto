from django.conf.urls import url
from . import views

app_name = 'inventory'

urlpatterns = [
    # /inventory/
    url(r'^$', views.index, name='index'),

]