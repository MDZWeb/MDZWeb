from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,email,username,contact_no,password=None):
        if not email:
            return ValueError('Email field is required')

        if not username:
            return ValueError('Username field is required')

        user=self.model(
            email=email,
            username=username,
            contact_no=contact_no
        )

        user.set_password(password)
        user.is_active=True
        user.save()

        return user

    def create_superuser(self,email,username,contact_no,password=None):
        if not email:
            return ValueError('Email field is required')

        if not username:
            return ValueError('Username field is required')

        user=self.model(
            email=email,
            username=username,
            contact_no=contact_no
        )

        user.set_password(password)
        user.is_active=True
        user.is_staff=True
        user.is_admin=True
        user.is_superadmin=True
        user.save()

        return user
        


class User(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=300,blank=True)
    last_name=models.CharField(max_length=300,blank=True)
    username=models.CharField(max_length=300)
    email=models.CharField(max_length=500,unique=True)
    contact_no=models.CharField(max_length=300,blank=True)
    password=models.CharField(max_length=700)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','contact_no']

    objects=UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self, app_label):
        return True

    # def get_user_permissions(self, obj=None):
    #     return True


