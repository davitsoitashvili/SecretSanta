from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self,email,name,surname,age,password):
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            surname = surname,
            age = age,
            password = password
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,name,surname,age,password):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            age=age,
            password = password
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','surname', 'age']

    objects = UserManager()

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label=None):
        return self.is_admin

    def __str__(self):
        return self.email

    def get_username(self):
        return f"{self.name} {self.surname}"







