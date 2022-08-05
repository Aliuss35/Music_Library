from django.urls import path
from . import views

urlpatterns = [
  path('', views.musics_list),
  path('<int:pk>/', views.musics_detail)


]