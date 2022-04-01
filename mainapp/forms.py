from django import forms
from django.contrib.auth. models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ProductReview

# Review Add Form
class ReviewAdd(forms.ModelForm):
     class Meta:
          model=ProductReview
          fields=('review_text','review_rating')