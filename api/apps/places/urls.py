from django.urls import URLPattern, path
from .views import PlaceAPIView, PlaceAPIGetUpdateDeleteView



urlpatterns = [
    path('', PlaceAPIView.as_view()),
    path('<int:id>/', PlaceAPIGetUpdateDeleteView.as_view()),
]

