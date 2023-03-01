from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    #: /app/
    path('', views.index, name="index"),
    #ex: /app/1/
    path('<int:question_id>/', views.details, name="details"),
    #: /app/1/results/
    path('<int:question_id>/results/', views.results, name="results"),
    #: /app/1/votes
    path('<int:question_id>/votes/', views.votes, name="votes"),
    #: /app/sample_error_500
    path('500', views.sample_error_500, name="500_error"),
]