from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import Http404
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import ListView, DetailView
from django_countries import countries
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(page)
        return render(
            request,
            "rooms/home.html",
            context={"rooms": rooms},
        )
    except EmptyPage:
        # rooms = paginator.page(1)
        return redirect("/")


class HomeView(ListView):
    """ HomeView Definitaion """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    page_kwarg = "page"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404()


class ModelNameDetail(DetailView):
    model = models.Room


def search(request):
    city = request.GET.get("city", "")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        context={"city": city, "countries": countries, "room_types": room_types},
    )
