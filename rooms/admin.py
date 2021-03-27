from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Amenity, models.HouseRule, models.Facility)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "room_type",
                    "country",
                    "city",
                    "address",
                    "price",
                )
            },
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "More About the space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facility", "house_rule"),
            },
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "room_type",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
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
    raw_id_fields = ("host",)
    search_fields = ("=city", "^host__username")
    filter_horizontal = (
        "amenities",
        "facility",
        "house_rule",
    )

    def save_model(self, request, obj, form, change):
        # obj.user = request.user
        super().save_model(request, obj, form, change)

    def count_amenities(self, obj):
        # obj <= room model
        # obj.amenities <= query set
        # obj.amenities.count <= function
        # obj.amenities.count() <= integer
        return obj.amenities.count()

    count_amenities.short_description = "Count of Amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ photo admin definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="200px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "thumbnail"
