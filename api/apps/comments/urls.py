from django.urls import path
from .views import CommentView, CommentSingleView


urlpatterns = [
    path('', CommentView.as_view()),
    path('<int:id>/', CommentSingleView.as_view())
    ]