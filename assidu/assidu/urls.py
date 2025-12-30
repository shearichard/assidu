from django.urls import path, include
from . import views

'''
urlpatterns = [
    path(
        "polls-non-nea/",
        views.citylist, 
        name="city_list_index"),
]
'''
urlpatterns = [
	path('', views.city_list, name='city_list'),
]

