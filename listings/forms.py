from django import forms
from .models import Client, Fournisseur, Medicament, Commande

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du client'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}),
        }

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du fournisseur'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}),
        }

class MedicamentForm(forms.ModelForm):
    class Meta:
        model = Medicament
        fields = ['nom', 'quantite_stock', 'prix', 'fournisseur']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du médicament'}),
            'quantite_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité en stock'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Prix'}),
            'fournisseur': forms.Select(attrs={'class': 'form-control'}),
        }

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client', 'medicament', 'quantite']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'medicament': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }