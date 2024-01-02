import gh.views
from django.urls import path

urlpatterns = [
    path("", gh.views.index)
]