from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15, blank=True)
    ville = models.CharField(max_length=100, blank=True)  # ✅ AJOUTER
    adresse = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nom

class Fournisseur(models.Model):
    id = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return self.nom

class Medicament(models.Model):
    id = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    nom = models.CharField(max_length=100)
    quantite_stock = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    
class Livreur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nom

class Commande(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]
    
    id = models.AutoField(primary_key=True)
    date_commande = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')
    livreur = models.ForeignKey(Livreur, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Commande {self.id} par {self.client.nom}"
    
