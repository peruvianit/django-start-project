from django.urls import path

from .views import authentication
from .views import questions

app_name = "app"

urlpatterns = [
    #: /login/
    path('login/', authentication.login, name="login"),
    #: /home/
    path('', authentication.index, name="index"),
    #: /app/
    path('questions', questions.list, name="list"),
    #ex: /app/1/
    path('<int:question_id>/', questions.details, name="details"),
    #: /app/1/results/
    path('<int:question_id>/results/', questions.results, name="results"),
    #: /app/1/votes
    path('<int:question_id>/votes/', questions.votes, name="votes"),
    #: /app/sample_error_500
    path('500', authentication.sample_error_500, name="500_error"),
]