from django import forms
from django.db.models.query import QuerySet
from django_countries.fields import CountryField
from pkg_resources import require
from . import models


class SearchForm(forms.Form):
    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KR").formfield()
    price = forms.IntegerField()
    room_type = forms.ModelChoiceField(
        empty_label="Any Kind", queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    super_host = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    facilities = forms.ModelMultipleChoiceField(
        models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
