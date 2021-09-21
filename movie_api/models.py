from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=300)

    class Meta:
        db_table = "movie"

    def avg_rating(self):
        all_ratings = Rating.objects.filter(movie=self)
        sum_of_ratings = 0
        for rating in all_ratings:
            sum_of_ratings += rating.rating
        no_of_ratings = len(all_ratings)
        if no_of_ratings > 0:
            return sum_of_ratings / no_of_ratings
        return sum_of_ratings

    def no_of_ratings(self):
        all_ratings = Rating.objects.filter(movie=self)
        return len(all_ratings)

    # def __str__(self):
    #     return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        unique_together = ('movie', 'user')
        index_together = ('movie', 'user')
        db_table = "rating"

    def __str__(self):
        return self.rating



