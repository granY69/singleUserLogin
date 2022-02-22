from django.urls import path
from . import views

urlpatterns = [
    path('mysecretadmins/51we113/register/', views.register),
    path('logout/', views.logout_user, name="logout_url"),
    path('login/', views.login_user, name='login_url')
]