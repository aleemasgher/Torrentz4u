from django .views import generic
from .models import Movies, Hollywood, Bollywood, Series
from django.shortcuts import render, get_object_or_404
import operator
from django.db.models import Q
from functools import reduce


class IndexView(generic.ListView):
    model = Movies
    template_name = 'movie/index.html'

def detail(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)
    return render(request, 'movie/detail.html', {'movie': movie})

class Holly(generic.ListView):
    model = Hollywood
    template_name = 'movie/hollywood.html'
    context_object_name = 'all_movie'
    paginate_by = 2
    queryset = Hollywood.objects.all()

def HollyDetail(request, movie_id):
    movie = get_object_or_404(Hollywood, pk=movie_id)
    return render(request, 'movie/holly_detail.html', {'movie': movie})

class Bolly(generic.ListView):
    model = Hollywood
    template_name = 'movie/bollywood.html'
    context_object_name = 'all_movie'
    paginate_by = 2
    queryset = Bollywood.objects.all()

def BollyDetail(request, movie_id):
    movie = get_object_or_404(Bollywood, pk=movie_id)
    return render(request, 'movie/bolly_detail.html', {'movie': movie})

class Seriess(generic.ListView):
    model = Series
    template_name = 'movie/series.html'
    context_object_name = 'all_movie'
    paginate_by = 2
    queryset = Series.objects.all()

def SeriesDetail(request, movie_id):
    movie = get_object_or_404(Series, pk=movie_id)
    return render(request, 'movie/series_detail.html', {'movie': movie})

def contactview(request):
    return render(request, 'movie/contact.html')

class SearchListView(generic.ListView):
    model = Movies
    context_object_name = 'all_movie'
    template_name = 'movie/search.html'

    def get_queryset(self):
        result = super(SearchListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(movie_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(movie_year__icontains=q) for q in query_list))
            )
        return result

