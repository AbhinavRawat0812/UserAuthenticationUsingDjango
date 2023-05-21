from django.urls import path
from . import views
from .views import UserLoginView,UserRegistrationView

urlpatterns = [
    # path('create-user/', views.create_user, name='create_user'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('select-users/', views.select_users, name='select_users'),
    path('register/',UserRegistrationView.as_view(),name='register_suer'),
]
