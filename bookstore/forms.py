import re

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField
from django.utils.text import phone2numeric

from bookstore.models import Review, CustomUser


class UserModelForm(ModelForm):
    confirm_password = CharField(max_length=255, required=True)
    class Meta:
        model = CustomUser
        fields = 'first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password'

    def clean_confirm_password(self):
        password = self.data.get("password")
        confirm_password = self.data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError('Passwords do not match!')

    def clean_password(self):
        return make_password(self.cleaned_data.get("password"))

    def clean_phone_number(self):
        phone = self.data.get('phone_number')
        return re.sub(r'\D', '', phone)

    def save(self, commit = True):
        data = self.cleaned_data
        data.pop('confirm_password')
        email = data.get('email')
        new_user = CustomUser(username=email, **data)
        return new_user.save()

class UserLoginModelForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = 'email', 'password'

class ReviewModelForm(ModelForm):
    class Meta:
        model = Review
        fields = 'book', 'review_text', 'user_name', 'rating'
