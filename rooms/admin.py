from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.HouseRule, models.Facility)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")},),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        (
            "More About the space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facility", "house_rule"),
            },
        ),
        ("Last Details", {"fields": ("host",)},),
    )

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
        "count_amenities",
    )

    # default ordering value
    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facility",
        "house_rule",
        "city",
        "country",
    )
    search_fields = ("=city", "^host__username")
    filter_horizontal = (
        "amenities",
        "facility",
        "house_rule",
    )

    def count_amenities(self, obj):
        # obj <= room model
        # obj.amenities <= query set
        # obj.amenities.count <= function
        # obj.amenities.count() <= integer
        return obj.amenities.count()

    count_amenities.short_description = "Count of Amenities"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
