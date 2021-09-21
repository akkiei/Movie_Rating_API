from django.conf.urls import url, include
from rest_framework import routers
from movie_api import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieView)
router.register(r'ratings', views.RatingView)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'', include(router.urls))

]
