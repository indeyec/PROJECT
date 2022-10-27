from django.contrib import admin
from django.urls import path
from . import views
from .views import profile
from .views import LogoutView
from .views import ChangeUserInfoView
from .views import PasswordChangeView
from .views import DeleteUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about, name='about'),
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', views.index, name='home'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/password/change/', PasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),

]
