from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_registeration, name='user_registeration'),
    path('successful', views.redirect, name='sample/successful.html')

]

# Create your views here.


# def home(request):
