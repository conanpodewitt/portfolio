from django.urls import path
from . import views

app_name = 'me'
urlpatterns = [
    # ex: /me/
    path('', views.index, name='index'),
    # ex: /me/cv
    path('cv/', views.cv, name='cv')
]
