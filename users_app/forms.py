from django.forms import ModelForm
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = Users
        exclude = ('id',)


class GroupForm(ModelForm):
    class Meta:
        model = Groups
        exclude = ('id',)
