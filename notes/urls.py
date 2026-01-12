from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path("", views.home, name="home"),
    path('<int:note_id>/edit/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('<int:note_id>/delete/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
]