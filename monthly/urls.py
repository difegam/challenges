from django.urls import path

from . import views

app_name = "monthly"

urlpatterns = [
    path("<str:month>", views.monthly_challenge, name="route-january"),
]
