import datetime

from django import forms
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from .models import ProductReview, Customer


class ReviewAdd(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('review_text', 'review_rating')

    def clean(self):
        super(ReviewAdd, self).clean()
        review = self.cleaned_data.get('review_text')
        rating = self.cleaned_data.get('review_rating')

        if not review:
            self._errors['review_text'] = self.error_class(['Пожалуйста, заполните это поле'])
        if not rating:
            self._errors['review_rating'] = self.error_class(['Пожалуйста, выюерите эемент в этом списке'])
        return self.cleaned_data


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def clean(self):
        super(ContactForm, self).clean()
        name = self.cleaned_data.get('name')
        subject = self.cleaned_data.get('subject')
        message = self.cleaned_data.get('message')

        if not name:
            self._errors['name'] = self.error_class(['Please, enter your name'])
        if not subject:
            self._errors['subject'] = self.error_class(['Please, enter your subject'])
        if not message:
            self._errors['message'] = self.error_class(['Please, enter your message'])
        return self.cleaned_data


class Profile(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'address']


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class CardValidation(forms.Form):
    cc_number = CardNumberField(label='Card Number', min_length=16, max_length=16)
    cc_expiry = CardExpiryField(label='Expiration Date', widget=DatePickerInput)
    cc_code = SecurityCodeField(label='CVV/CVC', min_length=3, max_length=3, widget=forms.PasswordInput())

    def clean(self):
        super(CardValidation, self).clean()
        cc_expiry = self.cleaned_data.get('cc_expiry')

        if cc_expiry < datetime.date.today():
            print('ERROR')
            self._errors['cc_expiry'] = self.error_class(['Your card has expired'])

