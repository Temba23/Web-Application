from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin

from PIL import Image
from django.core.validators import MinLengthValidator, int_list_validator
from django.urls import reverse


# Create your models here.
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=20)
#     email = models.EmailField(required=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pp = models.ImageField(default="lbj.jpg", upload_to="profile_pics")
    location = models.TextField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_no = models.CharField(verbose_name="Phone number", max_length=10, validators=[int_list_validator(sep=''), MinLengthValidator(10)], 
                                null=True, blank=True)

    def __str__(self): 
        return f"{self.user.username} Profile"
    
    class Meta:
        verbose_name_plural = 'Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.pp.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pp.path)

    def get_absolute_url(self):

        return reverse("profile-detail", kwargs={"pk": self.pk})