from django.contrib import admin
from .models import Client, Fournisseur, Medicament, Commande,Livreur 

class LivreurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'telephone')
    search_fields = ('nom', 'telephone')
    list_filter = ('nom',)


# Personnalisation de l'affichage des clients
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'telephone', 'adresse')  # Ajoute adresse
    search_fields = ('nom', 'telephone', 'adresse')
    list_filter = ('nom',)
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
    list_display = ('id', 'client', 'medicament', 'quantite', 'date_commande', 'statut', 'livreur')
    search_fields = ('client__nom', 'medicament__nom', 'livreur__nom')
    list_filter = ('date_commande', 'statut', 'client', 'medicament', 'livreur')
    list_editable = ('statut',)
# Enregistrement des modèles avec leurs classes Admin personnalisées
admin.site.register(Client, ClientAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Medicament, MedicamentAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Livreur, LivreurAdmin)
