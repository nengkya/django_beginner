from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

#create your views here
def homePageView(request):
    #there are three ways of inserting a style sheet: external CSS; internal CSS inline CSS
    return HttpResponse('<h1 style=color:green> Django for Beginner 2.1 2018 </h1>')

class HomePageView(TemplateView):
    template_name = 'home.html'
