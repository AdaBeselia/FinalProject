from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("general", views.general, name="general"),
    path("organization", views.organization, name="organization"),
    path("personnel", views.personnel, name="personnel"),
    path("timeframe", views.timeframe, name="timeframe"),
    path("budget", views.budget, name="budget")
]