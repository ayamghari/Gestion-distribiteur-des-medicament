from django.contrib import admin
from .models import Client, Fournisseur, Medicament, Commande

# Personnalisation de l'affichage des clients
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'telephone')  # Colonnes affichées dans la liste
    search_fields = ('nom', 'telephone')  # Ajoute une barre de recherche
    list_filter = ('nom',)  # Ajoute des filtres sur le côté

# Personnalisation de l'affichage des fournisseurs
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'telephone')
    search_fields = ('nom', 'telephone')
    list_filter = ('nom',)


# Personnalisation de l'affichage des médicaments
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'quantite_stock', 'prix', 'fournisseur')
    search_fields = ('nom', 'fournisseur__nom')  # Recherche par nom de médicament ou de fournisseur
    list_filter = ('fournisseur',)  # Filtre par fournisseur

# Personnalisation de l'affichage des commandes
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'medicament', 'date_commande')  # Colonnes affichées
    search_fields = ('client__nom', 'medicament__nom')  # Recherche par nom de client ou de médicament
    list_filter = ('date_commande', 'client', 'medicament')  # Filtres par date, client et médicament

# Enregistrement des modèles avec leurs classes Admin personnalisées
admin.site.register(Client, ClientAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Medicament, MedicamentAdmin)
admin.site.register(Commande, CommandeAdmin)