from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.date_list, name = 'date_list'),
    path('accounts/logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/login/', auth_view.LoginView.as_view(), name='login'),
    path('challenge/<int:pk>/', views.challenge_rules, name="challenge_rules"),
    path('challenge/new/',views.challenge_new,name='challenge_new'),
    path('register/', views.register, name="register"),
    path('challenge/<int:pk>/newentry/',views.entry_new, name="entry_new"),
    path('challenge/<int:pk>/resutls/',views.results_check, name="results"),
]
