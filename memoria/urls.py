from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('jogo/', views.jogo, name='jogo'),
    path('ranking/', views.ranking_view, name='ranking'),
]
