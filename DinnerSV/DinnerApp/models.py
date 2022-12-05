from django.db import models
from django.contrib.auth.models import  AbstractUser ,AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    es_cliente= models.BooleanField(default=False)
    es_gerente= models.BooleanField(default=False)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

#programar los modemos que faltan.
class Gerente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    

class Restaurante(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=15)
    direccion = models.CharField(max_length=30)
    capacidad = models.IntegerField()
    redesSociales = models.CharField(max_length=50)
    paginaWeb = models.CharField(max_length=40)
    gerente = models.ForeignKey(Gerente,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
















# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, user_name, password, **other_fields):

#         if not email:
#             raise ValueError(_("Debes ingresar un Email"))


#         email =self.normalize_email(email)
#         user = self.model(email=email,user_name=user_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user
#     def create_superuser(self, email, user_name, password, **other_fields):
        
        
        
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         return self.create_user(email,user_name,password,**other_fields)

    

# class CustomUser(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(_("email address"), max_length=254, unique=True)
#     user_name = models.CharField(max_length=150,unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active= models.BooleanField(default=False)
#     es_cliente = models.BooleanField(default=False)
#     es_gerente = models.BooleanField(default=False)

#     objects =  CustomUserManager()

#     USERNAME_FIELD =  'email'
#     REQUIRED_FIELDS =  ['user_name']

#     def __str__(self):
#         return str(self.user_name)

    


# class Cliente(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)














# class CustomUser(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN",'Admin'
#         CLIENTE = "CLIENTE", 'Cliente'
#         GERENTE = "GERENTE", 'Gerente'

#     base_role = Role.ADMIN
#     role = models.CharField(max_length=50, choices=Role.choices, default=Role.CLIENTE)
    
#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save()

# class ClienteManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(CustomUser.Role.CLIENTE)


# class Cliente(CustomUser):


    
#     base_role = CustomUser.Role.CLIENTE

#     cliente = ClienteManager()

#     class Meta:
#         proxy = True

# @receiver(post_save, sender=Cliente)
# def _post_save_receiver(sender,instance,created, **kwargs):
#     if created and instance.role == "CLIENTE":
#         ClienteProfile.objects.create(user=instance)

# class ClienteProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     cliente_id = models.IntegerField(null=True,blank=True)
    



# class GerenteManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(CustomUser.Role.GERENTE)




# class Gerente(CustomUser):


    
#     base_role = CustomUser.Role.GERENTE

#     gerente = GerenteManager()

#     class Meta:
#         proxy = True

# @receiver(post_save, sender=Gerente)
# def _post_save_receiver(sender,instance,created, **kwargs):
#     if created and instance.role == "GERENTE":
#         GerenteProfile.objects.create(user=instance)

# class GerenteProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     gerente_id = models.IntegerField(null=True,blank=True)
    

# Create your models here.
# class Restaurates(models.Model):
#     nombre= models.CharField(max_length=50)
#     dueño= 

