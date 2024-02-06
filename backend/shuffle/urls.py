from django.urls import path
from shuffle.views import Shuffler

urlpatterns = [
    path('', Shuffler.as_view()),
]
