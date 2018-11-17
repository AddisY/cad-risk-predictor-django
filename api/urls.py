from django.urls import path

from api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name='api'

urlpatterns = [
    path('symptoms',views.SymptomsView.as_view(),name='symptoms'),
    path('signup/doctor',views.DoctorSignupView.as_view(),name='doctor-signup'),#temporary
    path('signup/user',views.OrdinaryUserView.as_view(),name='user-signup'),
    path('analyze-data', views.analyse_data, name='analyze-data'),
    path('analyze-data-test', views.TestDataView.as_view(), name='analyze-data-test'),

    #path('login',views.Login.as_view(),name='user-signup'),
    path('api-token-auth/',obtain_auth_token),

]
