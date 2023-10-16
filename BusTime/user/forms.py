from django import forms

class BusScheduleSearch(forms.Form):
    b_from=forms.CharField(label='From',max_length=100)
    to=forms.CharField(label='To',max_length=100)