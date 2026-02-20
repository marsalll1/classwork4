from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view())
]