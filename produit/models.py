from django.db import models



class Tag(models.Model):
    nom = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.nom



class Produit(models.Model):
    nom = models.CharField(max_length=100,null=True)
    tag = models.ManyToManyField(Tag)
    prix = models.PositiveIntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom