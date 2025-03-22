from django.urls import path
from .views import homePageView, HomePageView

urlpatterns = [

    #<a href="{% url 'home' %}"> Home </a>
    #path('', homePageView, name = 'home')

    path('', HomePageView.as_view(), name = 'home')

]
