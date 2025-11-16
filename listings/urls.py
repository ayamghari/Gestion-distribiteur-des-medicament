from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),  
    
    # Authentification
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),

    # Clients
    path('liste-clients/', views.liste_clients, name='liste_clients'),
    path('modifier-client/<int:id>/', views.modifier_client, name='modifier_client'),
    path('supprimer-client/<int:id>/', views.supprimer_client, name='supprimer_client'),
    path('ajouter-client/', views.ajouter_client, name='ajouter_client'),

    # Fournisseurs
    path('liste-fournisseurs/', views.liste_fournisseurs, name='liste_fournisseurs'),
    path('modifier-fournisseur/<int:id>/', views.modifier_fournisseur, name='modifier_fournisseur'),
    path('supprimer-fournisseur/<int:id>/', views.supprimer_fournisseur, name='supprimer_fournisseur'),
    path('ajouter-fournisseur/', views.ajouter_fournisseur, name='ajouter_fournisseur'),

    # Médicaments
    path('liste-medicaments/', views.liste_medicaments, name='liste_medicaments'),
    path('modifier-medicament/<int:id>/', views.modifier_medicament, name='modifier_medicament'),
    path('supprimer-medicament/<int:id>/', views.supprimer_medicament, name='supprimer_medicament'),
    path('ajouter-medicament/', views.ajouter_medicament, name='ajouter_medicament'),

    # Commandes
    path('liste-commandes/', views.liste_commandes, name='liste_commandes'),
    path('modifier-commande/<int:id>/', views.modifier_commande, name='modifier_commande'),
    path('supprimer-commande/<int:id>/', views.supprimer_commande, name='supprimer_commande'),
    path('ajouter-commande/', views.ajouter_commande, name='ajouter_commande'),
]