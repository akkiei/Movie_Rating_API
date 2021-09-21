from rest_framework import serializers
from movie_api import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['id', 'title', 'description', 'avg_rating', 'no_of_ratings']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = ['id', 'rating', 'user', 'movie']


# class RatedMovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Movie
#         fields = ['id', 'avg_rating', 'title']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
