from . import views
from django.urls import path
urlpatterns = [
    path('', views.index,name="index"),
    path('service/', views.service,name="service"),
    path('about/', views.about,name="about"),
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
    path('functionLogin/', views.functionLogin,name="functionLogin"),
    path('forgot_password/', views.forgot_password,name="forgot_password"),
    path('forgot_username/', views.forgot_username,name="forgot_username"),
    path('contactValidate/', views.contactValidate,name="contactValidate"),
    ]