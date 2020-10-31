from django.contrib.gis import forms

from worker.models import Tracking


class TrackingForm(forms.ModelForm):
    class Meta:
        model = Tracking
        exclude = ["nothing"]

    gps = forms.PointField(widget=forms.OSMWidget(attrs={
        'map_width': 800,
        'map_height': 500,
    }))
