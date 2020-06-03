from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Requester


class RequesterCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Requester
        fields = ('username', 'email')

class RequesterChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Requester
        fields = ('username', 'email')