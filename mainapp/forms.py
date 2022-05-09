from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ProductReview


# Review Add Form
class ReviewAdd(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('review_text', 'review_rating')


class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
