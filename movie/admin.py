from django.contrib import admin
from .models import Series, Torrents, Hollywood, Bollywood, Movies

admin.site.register(Movies)
admin.site.register(Torrents)
admin.site.register(Hollywood)
admin.site.register(Bollywood)
admin.site.register(Series)