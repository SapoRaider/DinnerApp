from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    tipo_usuario = [('1', 'Gerente'),('2','Cliente')]
    username = forms.EmailField(required=True, label='Email')
    Nombre = forms.CharField(max_length=254,label="Nombre Completo")
    numero = forms.IntegerField(label='Numero de telefono')
    tipo = forms.ChoiceField(choices=tipo_usuario, widget=forms.RadioSelect)



    Nombre.widget.attrs['class'] = 'form-control'
    username.widget.attrs['class'] = 'form-control'
    numero.widget.attrs['class'] = 'form-control'


    def __init__(self, *args, **kwargs) -> None:
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class meta:
        Model = User
        fields = ('email','name','numero','password1', 'password2')
        help_texts = {k:"" for k in fields}

