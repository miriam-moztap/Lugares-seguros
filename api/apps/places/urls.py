from django.urls import URLPattern, path
from .views import PlaceAPIView, PlaceAPIUpdateDeleteView, PlaceGetAPIView


urlpatterns = [
    path('', PlaceAPIView.as_view()),    
    path('<int:id>/', PlaceGetAPIView.as_view()),
    path('<int:id>/', PlaceAPIUpdateDeleteView.as_view()),
]
