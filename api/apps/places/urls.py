from django.urls import URLPattern, path
from .views import PlaceAPIView, PlaceAPIUpdateDeleteView, PlacegetView


urlpatterns = [
    path('', PlaceAPIView.as_view()),
    path('<int:id>/', PlacegetView.as_view()),
    path('<int:id>/', PlaceAPIUpdateDeleteView.as_view()),
]
