from django.db import models
from django.contrib.auth.models import  AbstractUser ,AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email,name,numero ,password, is_staff, is_superuser,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            numero=numero,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None,name=None,numero=None,password=None, **extra_fields):
        return self._create_user(email,name,numero,password, False, False, **extra_fields)

    def create_superuser(self, email,name,numero, password, **extra_fields):
        user = self._create_user(email,name,numero, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, blank=True)
    numero = models.IntegerField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name','numero']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    def get_email(self):
        return self.email


class user_type(models.Model):
    es_cliente = models.BooleanField(default=False)
    es_gerente = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.es_cliente == True:
            return User.get_email(self.user) + " - es_cliente"
        else:
            return User.get_email(self.user) + " - es_gerente"



    

class Restaurante(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=254)
    categoria = models.CharField(max_length=35)
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=15)
    direccion = models.CharField(max_length=30)
    capacidad = models.IntegerField()
    redesSociales = models.CharField(max_length=50)
    paginaWeb = models.CharField(max_length=40)
    gerente = models.ForeignKey(User, on_delete=models.CASCADE)
    # gerente = models.ForeignKey(Gerente,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# class Menu(models.Model):
#     platos = models.


class Reservacion(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    menu = models.OneToOneField()