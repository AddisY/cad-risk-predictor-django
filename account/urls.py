"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from account import views

app_name='account'

urlpatterns = [
    path('signup/doctor', views.signup_doctor,name='signup_doctor'),
    path('signup/user',views.signup_ordinary_user,name='signup_ordinary_user'),
    path('login', views.user_login, name='login'),
    path('home',views.home_page,name='home'),
    path('save-data',views.save_data ,name='save_data'),
    path('logout',views.logout_view,name='logout'),
    path('check-symptoms', views.check_symptoms_view, name='check symptoms'),
    path('check-symptoms/<int:pk>',views.check_symptoms_view,name='check symptoms'),
    path('analyze-data',views.analyze_data ,name='analyze data')
]


""" 
    path('signup/user'),
  path('logout/','django.contrib.auth.view.logout',name='logout'),
    path('logout-then-login/', 'django.contrib.auth.view.logout_then_login', name='logout_then_login'),
   

"""