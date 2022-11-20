from django.urls import path
from . import views

app_name = 'movieapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('Movie/<int:id>/', views.detail, name="details"),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
