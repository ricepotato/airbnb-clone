from django.urls import path
from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>", views.room_detail, name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]
