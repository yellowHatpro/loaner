from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/signup/', views.signup, name='signup'),
    path('api/login/', auth_views.LoginView.as_view(
        template_name='core/login.html',
        authentication_form=LoginForm,
        ), name='login'),
    path('api/logout/', views.logout_view, name='logout')
]