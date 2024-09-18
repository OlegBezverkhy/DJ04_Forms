from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

MOVIES_PER_PAGE = 3

def index(request):
    return render(request, 'films/index.html')


def add_movie(request):
    error = ''
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Error'
    form = MovieForm()
    return render(request, 'films/add_movie.html', {'form': form, 'errors': error})


def movie_list(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, MOVIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'films/movie_list.html', {'page_obj': page_obj})