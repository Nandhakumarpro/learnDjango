from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_password(value):
    print("validate_password")
    '''Following is the pattern for
    Minimum eight characters, at least one letter, one number and one special character:
    '''
    patn = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    if not re.match(patn, value) :
        raise ValidationError(
        _('''%(value)s is not a valid pattern!!!,
        Password Should contains Minimum eight characters, at least one letter, one number and one special character'''),
        params={'value': "password"},
    )
    return

class UserForm(forms.ModelForm):
    password = forms.CharField(required = False, validators = [validate_password ,] )
    class Meta:
        model = User
        fields = "__all__"#("username","password")

    def clean_password(self):
        print("clean_password")
        return self.cleaned_data["password"]

class TestForm(forms.Form):
    test = forms.IntegerField(required = True)
    def clean_test(self):
        return self.cleaned_data["test"] + 1
    class Meta:
        fields = "__all__"


class UserForm2 (forms.Form):

    username = forms.CharField( required=True)
    password = forms.CharField( required=True)

    def clean_password(self):

        try:
            int (self.cleaned_data["password"])
        except :
            raise ValidationError("password must be a number...")
        return self.cleaned_data["password"]

    class Meta:
        fields = "__all__"

class ProjectForm(forms.Form):
    pass
