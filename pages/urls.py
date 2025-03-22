from django.urls import path
from .views import homePageView, HomePageView, AboutPageView

urlpatterns = [

    #<a href="{% url 'home' %}"> Home </a>
    #path('', homePageView, name = 'home')

    path('', HomePageView.as_view(), name = 'home'),

    path('about/', AboutPageView.as_view(), name = 'about')

]
