from django import forms
from .models import Reservation
from .widgets import DatePickerWidget

class ReservationSearchForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('checkin', 'checkout', 'adults', 'kids',)
        widgets = {
            'checkin':DatePickerWidget,
            'checkout':DatePickerWidget
        }
        