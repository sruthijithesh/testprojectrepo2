from django.urls import path
from . import views
urlpatterns = [
    path('login', views.loginfn, name='login'),
    path('submit', views.submitfn, name='submit')
    
]