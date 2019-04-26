from django import forms
from .models import Challenge, Entries

class ChallengeForm(forms.ModelForm):

    class Meta:
        model = Challenge
        fields = ('title','prize','rules','end_date')

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entries
        fields = ('total',)
