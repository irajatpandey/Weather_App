# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('getTemperature', views.getTemperature, name='getTemperature')

   
]