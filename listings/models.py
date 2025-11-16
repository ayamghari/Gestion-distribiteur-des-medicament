from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)

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

class Commande(models.Model):
    id = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    date_commande = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)

    def __str__(self):
        return f"Commande {self.id} par {self.client.nom}"