from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/movie_list.html', {'movies': movies})

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_app/movie_details.html', {'movie': movie})    

def search_movies(request):
    title_query = request.GET.get('title')
    genre_query = request.GET.get('genre')
    year_query = request.GET.get('year')
    
    return render(request, 'movie_app/movie_search.html', {'movies': movies})

