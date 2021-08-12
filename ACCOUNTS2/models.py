from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class MOTHER(models.Model):
    CATEGORY = (
        ('1','1'),
        ('2','2'),
        ('3','3')
    )
    F_Name = models.CharField(max_length=100)
    L_Name = models.CharField(max_length=100)
    Reg_No = models.CharField(max_length=100)
    Email = models.EmailField()
    Select = models.CharField(max_length=100, choices=CATEGORY, null=True, blank=True)

class CHILD1(MOTHER):
    Age = models.IntegerField()


#Django signals
class PROFILE(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    Phone = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user)

