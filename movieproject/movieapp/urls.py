from django.urls import path, include
from . import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.addMovie,name='addMovie'),
    path('update/<int:id>/',views.updateMovie,name='update'),
    path('delete/<int:id>/',views.deleteMovie,name='delete'),

]
