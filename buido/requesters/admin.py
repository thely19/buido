from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RequesterCreationForm, RequesterChangeForm
from .models import Requester

class RequesterAdmin(UserAdmin):
    add_form = RequesterCreationForm
    form = RequesterChangeForm
    model = Requester

admin.site.register(Requester, RequesterAdmin)