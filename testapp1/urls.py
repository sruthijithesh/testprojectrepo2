from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.homefn, name='home'),
    path('outside',views.outsidefn, name='outside')
]