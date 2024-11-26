"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from task2.views import Class_template, func_template
#from task3.views import home_page, game_page, cart_page
from task4.views import home_page, game_page, cart_page
from task5.views import sign_up_by_django, sign_up_by_html
#from django.http import HttpResponse
#def home_view(request):
    #return HttpResponse("<h1>Welcome to UrbanDjango!</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', Class_template.as_view()),
    path('func/', func_template),
    path('platform/', home_page),
    path('games/', game_page),
    path('cart/', cart_page),
    path('', sign_up_by_django),
    path('sign/', sign_up_by_html)
    #path('', home_view, name='home'),

]