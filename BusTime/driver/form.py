from django import forms
from .models import Bustime
# from .models import Busroute

class TimeTable(forms.ModelForm):
    class Meta:
        model=Bustime
        fields="__all__"

# class route(forms.ModelForm):
#     class Meta:
#         model=Busroute
#         fields="__all__"