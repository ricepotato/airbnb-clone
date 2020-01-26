from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.HouseRule, models.Facility)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
