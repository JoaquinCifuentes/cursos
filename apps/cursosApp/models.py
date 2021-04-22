from __future__ import unicode_literals
from django.db import models

class CursosManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}

        if len(postData["name"])<5:
            errors["name"]="el nombre del curso debe tener mas de 5 caracteres"
        if len(postData["desc"])<15:
            errors["desc"]="la descripcion debe tener almenos 15 caracteres"
        return errors

class Descripciones(models.Model):
    desc=models.TextField()


class Cursos(models.Model):
    name = models.CharField(max_length=200)
    desc = models.OneToOneField(Descripciones, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CursosManager()



# Create your models here.
