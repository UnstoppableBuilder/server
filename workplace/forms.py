from django.contrib.gis import forms

from workplace.models import Zone


class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        exclude = ["nothing"]

    poly = forms.PolygonField(widget=forms.OSMWidget(attrs={
        'map_width': 800,
        'map_height': 500,
        'default_lat': 55.751244,
        'default_lon': 37.618423
    }))
