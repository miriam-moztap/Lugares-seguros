from django.urls import URLPattern, path
from .views import CommentView, CommentSingleView

urlpatterns = [
    path('', CommentView.as_view()),
    path('<int:pk>/', CommentSingleView.as_view()),
]   