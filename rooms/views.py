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
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    room_types = models.RoomType.objects.all()

    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    instant = bool(request.GET.get("instant", False))
    super_host = bool(request.GET.get("super_host", False))

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    filter_args = {}
    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths_gte"] = baths

    if instant:
        filter_args["instant_book"] = True

    if super_host:
        filter_args["host__superhost"] = True

    if s_amenities:
        for s_a in s_amenities:
            filter_args["amenities__pk"] = int(s_a)

    if s_facilities:
        for s_f in s_facilities:
            filter_args["facilities__pk"] = int(s_f)

    rooms = models.Room.objects.filter(**filter_args)

    return render(
        request,
        "rooms/search.html",
        context={**form, **choices, "rooms": rooms},
    )
