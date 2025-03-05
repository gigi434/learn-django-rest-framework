from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def movie_list(request):
    """ すべての映画を取得するためのビュー関数 """
    # SQLiteデータベースから全ての映画を取得
    movies = Movie.objects.all()

    # シリアライザーを使ってデータをシリアライズ
    serializer = MovieSerializer(movies, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def movie_detail(request, pk):
    """ 1つの映画を取得するためのビュー関数 """
    # SQLiteデータベースから指定されたIDの映画を取得
    movie = Movie.objects.get(pk=pk)

    # シリアライザーを使ってデータをシリアライズ
    serializer = MovieSerializer(movie)

    return JsonResponse(serializer.data, safe=False)
