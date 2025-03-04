from django.urls import path
from watchlist_app.views import movie_list, movie_datail

urlpatterns = [
    path("list/", movie_list, name="movie-list"),
    path("<int:pk>", movie_datail, name="movie-detail"),
]
