<<<<<<< HEAD
from django.urls import URLPattern, path
=======
from django.urls import path
>>>>>>> 5357af978d8fc2f4f806b0e7f30ab53a00305135
from .views import CommentView, CommentSingleView


urlpatterns = [
    path('', CommentView.as_view()),
<<<<<<< HEAD
    path('<int:id>/',CommentSingleView.as_view()),
=======
    path('<int:pk>/', CommentSingleView.as_view()),
>>>>>>> 5357af978d8fc2f4f806b0e7f30ab53a00305135
    ]