from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CUSTOMACCOUNTMANAGER(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, **other_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, last_name=last_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("is_staff=True for SuperUser!")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("is_superuser=True for SuperUser!")

        return self.create_user(email, username, first_name, last_name, password, **other_fields)



class NEWUSER(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(blank=True, max_length=200)
    last_name = models.CharField(blank=True, max_length=200)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(blank=True, max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    user_type = models.CharField(max_length=200, blank=True)
    
    objects = CUSTOMACCOUNTMANAGER()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin



#My Users

class MYUSER(models.Model):
    user = models.OneToOneField(NEWUSER, on_delete=models.CASCADE)
    fName = models.CharField(max_length=200)
    lName = models.CharField(max_length=200)
    fAge = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class TEACHER(MYUSER):
    Role_No = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.fName

class STUDENT(MYUSER):
    Reg_No = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.fName

class PARENT(MYUSER):
    Phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.fName