from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('application/', views.application, name='application'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('createUser/', views.createUser, name='createUser'),
    path('signIn/', views.signIn, name='signIn'),
    path('signOut/', views.signOut, name='signOut'),
    path('submitApplication/', views.submitApplication, name='submitApplication')
]
