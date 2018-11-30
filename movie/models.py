from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_name = models.CharField(max_length=250)
    movie_year = models.CharField(max_length=4)
    movie_rating = models.CharField(max_length=10, null=True)
    description = models.TextField(null=True)
    cast = models.CharField(max_length=100, null=True)
    movie_logo = models.FileField()
    youTrailer_link = models.CharField(max_length=10000, null=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_name + ' - ' + self.movie_year

    class Meta:
        ordering = ["-created", "-update"]


class Hollywood(models.Model):
    holly = models.ForeignKey(Movies, on_delete=models.CASCADE)
    country = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.holly.movie_name + ' - ' + self.holly.movie_year + ' - ' + self.country


    class Meta:
        ordering = ["-created", "-update"]


class Bollywood(models.Model):
    bolly = models.ForeignKey(Movies, on_delete=models.CASCADE)
    country = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.bolly.movie_name + ' - ' + self.bolly.movie_year + ' - ' + self.country


    class Meta:
        ordering = ["-created", "-update"]


class Series(models.Model):
    series = models.ForeignKey(Movies, on_delete=models.CASCADE)
    category = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.series.movie_name + ' - ' + self.series.movie_year + ' - ' + self.category


    class Meta:
        ordering = ["-created", "-update"]


class Torrents(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    holly = models.ForeignKey(Hollywood, on_delete=models.CASCADE, null=True, blank=True)
    bolly = models.ForeignKey(Bollywood, on_delete=models.CASCADE, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True)
    file_type = models.CharField(max_length=350, null=True, blank=True)
    torrent_size = models.CharField(max_length=350, null=True, blank=True)
    torrent_Link = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.file_type


#usenamer "aleem607"
#password "mynameisaleemmalik"