from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

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


class reservacionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.restauranteid = kwargs.pop('restauranteid')
        super(reservacionForm, self).__init__(*args, **kwargs)
        self.fields['menu'].queryset = Menu.objects.filter(
            restaurante_id=self.restauranteid)


    def label_from_instance(self,obj):
        print("obj "+str(obj.id))
        return int(obj.id)
    horario = forms.TimeField(input_formats='%H:%M', required=True)
    menu = forms.ModelChoiceField(queryset=None)


    horario.widget.attrs['class'] = 'form-control'
    menu.widget.attrs['class'] = 'form-control'


class restauranteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    correo = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=254)
    categoria = forms.CharField(max_length=35)
    telefono = forms.IntegerField(max_value=99999999,min_value=1)
    ciudad = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=30)
    capacidad = forms.IntegerField(min_value=1)
    redesSociales = forms.CharField(max_length=50)
    paginaWeb = forms.CharField(max_length=40)

class menuForm(forms.Form):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        request = kwargs.pop('request')
        super(menuForm, self).__init__(*args, **kwargs)
        self.fields['restaurante'].queryset = Restaurante.objects.filter(
            gerente=request.user)

    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=600)
    restaurante = forms.ModelChoiceField(queryset=None)

