from django.db import models

class Commentaire(models.Model):
    date = models.DateField(auto_now=True)
    email = models.EmailField(max_length=150)
    contenu = models.TextField(max_length=750)
