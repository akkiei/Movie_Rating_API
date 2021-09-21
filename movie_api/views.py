from rest_framework import viewsets
from movie_api import models, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated, AllowAny
# for custom post function
from movie_api import models
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class MovieView(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @list_route(methods=['get'], url_path="get-rated-movies")
    def get_rated_movie(self, req):
        result = []
        user = req.user
        for p in models.Movie.objects.raw(
                "Select m.id, m.title, r.rating from movie m inner join rating r on m.id = r.\"movie_id\""):
            print(p.id, p.title, p.rating)
            result_dict = {
                "id": p.id,
                "title": p.title,
                "rating": p.rating,
                "user": str(user)

            }
            result.append(result_dict)
        return Response(result, status.HTTP_200_OK)

        # rated_movies = models.Movie.objects.raw(
        #     "Select m.id, m.title, r.rating from movie m inner join rating r on m.id = r.\"movie_id\"")
        # print(rated_movies)

        # serializer = serializers.MovieSerializer(rated_movies, many=False)
        # return Response(serializer.data, status.HTTP_200_OK)
    #
    #  THIS ONE REPLACES THE DEFAULT RESPONSE TO THE GET REQUEST OF LISTING ALL THE OBJECTS
    # def list(self, request, *args, **kwargs):
    #     result = []
    #     for p in models.Movie.objects.raw(
    #             "Select m.id, m.title, r.rating from movie m inner join rating r on m.id = r.\"movie_id\""):
    #         print(p.id, p.title, p.rating)
    #         result_dict = {
    #             "id": p.id,
    #             "title": p.title,
    #             "rating": p.rating
    #         }
    #         result.append(result_dict)
    #     return Response(result, status.HTTP_200_OK)

    # authentication_classes = (TokenAuthentication,)
    # detail_route gets pk(primary key)
    # list_route for entire list not one id
    # @detail_route(methods=['post'], url_path="add_movie")
    # def add_movie_rating(self, request, pk=None):
    #     if 'rating' in request.data:
    #         rating = request.data['rating']
    #         movie_title = models.Movie.objects.get(id=pk)
    #         user = User.objects
    #         print(user)
    #         return Response("", status.HTTP_200_OK)
    #     else:
    #         resp = {"message": "please enter ratings as well !!"}
    #         return Response(resp, status.HTTP_200_OK)


class RatingView(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    authentication_classes = (TokenAuthentication,)

    # this makes sure the user is logged in or not
    permission_classes = (IsAuthenticated,)
