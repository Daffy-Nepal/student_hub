from django import forms
from .models import Feedback


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'titleId'}),
            'description': forms.Textarea(attrs={'id': 'descriptionId'}),
        }
