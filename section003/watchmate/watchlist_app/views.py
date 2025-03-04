from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse


def movie_list(request):
    movies = Movie.objects.all()

    # moviesをJson形式で返すためには、QuerySet型のため、辞書型に変換した後でリスト型に変換する
    data = {"movies": list(movies.values())}
    return JsonResponse(data)


def movie_datail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        "name": movie.name,
        "description": movie.description,
        "activate": movie.activate
    }
    return JsonResponse(data)
