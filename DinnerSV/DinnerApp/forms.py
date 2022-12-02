from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    numero = forms.IntegerField(label='Numero de telefono')


    
    email.widget.attrs['class'] = 'form-control'
    numero.widget.attrs['class'] = 'form-control'


    def __init__(self, *args, **kwargs) -> None:
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class meta:
        Model = User
        fields = ('username','email','numero','password1', 'password2')
        help_texts = {k:"" for k in fields}

