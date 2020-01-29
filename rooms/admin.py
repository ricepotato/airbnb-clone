from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.HouseRule, models.Facility)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = ("city", "instant_book", "country")
    search_fields = ("city", "^host__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
