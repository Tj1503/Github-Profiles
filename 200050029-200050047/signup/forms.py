from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields={
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name'     
        }

    field_order=['username','password1','password2','first_name','last_name' ]

    def save(self,commit=True):
        user=super(RegForm, self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']

        if commit:
            user.save()

        return user