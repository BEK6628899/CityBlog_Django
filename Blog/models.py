from django.db import models


class Manzara(models.Model):
    joy_nomi = models.CharField(max_length=30)
    rasm = models.FileField()
    matn = models.CharField(max_length=5000)
    sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.joy_nomi


class Shaxar(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField()
    matn = models.CharField(max_length=1000)
    sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nom


class Din(models.Model):
    din_malumot = models.CharField(max_length=1000,null=True,blank=True)
    rasm = models.FileField(null=True,blank=True)
    shaxar = models.OneToOneField(Shaxar,on_delete=models.CASCADE,null=True,blank=True)
    vaqt = models.DateField(auto_now_add=True,blank=True,null=True)


class About(models.Model):
    rasm = models.FileField()






