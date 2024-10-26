from django import forms
from comments.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = 'user', 'review'
        widgets = {
            'user': forms.TextInput(attrs={'type': 'hidden'}),
            'review': forms.Textarea(attrs={'class': 'review-input', 'type': 'text'})
        }
