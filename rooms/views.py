from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import ListView
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
