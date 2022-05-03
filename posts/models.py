import PIL.Image
from django.db import models


# Create your models here.


class user(models.Model):
    kullanıcı_adı=models.CharField(max_length=150)
    dosya=models.FileField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.kullanıcı_adı

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=PIL.Image.open(self.image.path)

        if img.height>300 or img.weight>300:
            output_size=(2000,2000)
            img.thumbnail(output_size)
            img.save(self.image.path)

class about(models.Model):

    kul_ad=models.CharField(max_length=150)
    about_user=models.TextField()
    user_image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.kul_ad

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=PIL.Image.open(self.user_image.path)

        if img.height>300 or img.weight>300:
            output_size=(200,200)
            img.thumbnail(output_size)
            img.save(self.user_image.path)







