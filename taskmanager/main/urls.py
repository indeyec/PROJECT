from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about, name='about'),
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', views.index, name='home'),
]
