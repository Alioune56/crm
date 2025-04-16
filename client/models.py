from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom