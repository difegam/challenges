from django.urls import path

from . import views

# app_name = "monthly"

urlpatterns = [
    path("", views.monthly_challenges_list, name="all-challenges"),
    path("<int:month>", views.monthly_challenge_by_number, name="month-challenge-int"),
    path("<str:month>", views.monthly_challenge, name="month-challenge-str"),
]
