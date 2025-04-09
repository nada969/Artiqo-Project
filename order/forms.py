from django import forms
from .models import OrderArt

class OrderArtForm(forms.ModelForm):
    class Meta:
        model = OrderArt
        fields = ['user', 'artist_email', 'art_name', 'story']
        widgets = {
            'story': forms.Textarea(attrs={'rows': 8, 'cols': 40}),
        }
        labels = {
            'user': 'User',
            'artist_email': 'Artist email:',
            'art_name': 'Art name:',
            'story': 'Story:',
        }
        