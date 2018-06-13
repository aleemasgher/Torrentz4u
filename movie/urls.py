from django.conf.urls import url
from . import views

app_name = 'movie'

urlpatterns = [
    # /index/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /hollywood/
    url(r'^hollywood/$', views.Holly.as_view(), name='hollywood'),

    # /hollywood/id/
    url(r'hollywood/(?P<movie_id>[0-9]+)/$', views.HollyDetail, name='holly_detail'),

    # /bollywood/
    url(r'^bollywood/$', views.Bolly.as_view(), name='bollywood'),

    # /bollywood/id/
    url(r'bollywood/(?P<movie_id>[0-9]+)/$', views.BollyDetail, name='bolly_detail'),

    # /series/
    url(r'^series/$', views.Seriess.as_view(), name='series'),

    # /series/id/
    url(r'series/(?P<movie_id>[0-9]+)/$', views.SeriesDetail, name='series_detail'),

    # /contact/
    url(r'^contact/$', views.contactview, name='contact'),

    url(r'^search/$', views.SearchListView.as_view(), name='search'),

    # /search/id/
    url(r'search/(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
]
