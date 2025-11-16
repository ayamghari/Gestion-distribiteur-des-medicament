from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Fournisseur, Medicament, Commande
from .forms import ClientForm, FournisseurForm, MedicamentForm, CommandeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

@login_required
def accueil(request):
    return render(request, 'listings/accueil.html')

# === Clients ===
@login_required
def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'listings/liste_clients.html', {'clients': clients})

@login_required
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm()
    return render(request, 'listings/ajouter_client.html', {'form': form})

@login_required
def modifier_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'listings/modifier_client.html', {'form': form})

@login_required
def supprimer_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        client.delete()
        return redirect('liste_clients')
    return render(request, 'listings/supprimer_client.html', {'client': client})

# === Fournisseurs ===
@login_required
def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'listings/liste_fournisseurs.html', {'fournisseurs': fournisseurs})

@login_required
def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm()
    return render(request, 'listings/ajouter_fournisseur.html', {'form': form})

@login_required
def modifier_fournisseur(request, id):
    fournisseur = get_object_or_404(Fournisseur, id=id)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'listings/modifier_fournisseur.html', {'form': form})

@login_required
def supprimer_fournisseur(request, id):
    fournisseur = get_object_or_404(Fournisseur, id=id)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('liste_fournisseurs')
    return render(request, 'listings/supprimer_fournisseur.html', {'fournisseur': fournisseur})

# === Médicaments ===
@login_required
def liste_medicaments(request):
    medicaments = Medicament.objects.all()
    return render(request, 'listings/liste_medicaments.html', {'medicaments': medicaments})

@login_required
def ajouter_medicament(request):
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medicaments')
    else:
        form = MedicamentForm()
    return render(request, 'listings/ajouter_medicament.html', {'form': form})

@login_required
def modifier_medicament(request, id):
    medicament = get_object_or_404(Medicament, id=id)
    if request.method == 'POST':
        form = MedicamentForm(request.POST, instance=medicament)
        if form.is_valid():
            form.save()
            return redirect('liste_medicaments')
    else:
        form = MedicamentForm(instance=medicament)
    return render(request, 'listings/modifier_medicament.html', {'form': form})

@login_required
def supprimer_medicament(request, id):
    medicament = get_object_or_404(Medicament, id=id)
    if request.method == 'POST':
        medicament.delete()
        return redirect('liste_medicaments')
    return render(request, 'listings/supprimer_medicament.html', {'medicament': medicament})

# === Commandes ===
@login_required
def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'listings/liste_commandes.html', {'commandes': commandes})

@login_required
def ajouter_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save(commit=False)
            medicament = commande.medicament
            quantite = commande.quantite
            
            if medicament.quantite_stock == 0:
                messages.error(request, f'Stock vide pour {medicament.nom}!')
            elif medicament.quantite_stock >= quantite:
                medicament.quantite_stock -= quantite
                medicament.save()
                commande.save()
                messages.success(request, 'Commande créée!')
                return redirect('liste_commandes')
            else:
                messages.error(request, f'Stock insuffisant! Disponible: {medicament.quantite_stock}')
    else:
        form = CommandeForm()
    return render(request, 'listings/ajouter_commande.html', {'form': form})

@login_required
def modifier_commande(request, id):
    commande = get_object_or_404(Commande, id=id)
    ancien_medicament = commande.medicament
    ancienne_quantite = commande.quantite
    
    
    
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            nouvelle_commande = form.save(commit=False)
            nouveau_medicament = nouvelle_commande.medicament
            nouvelle_quantite = nouvelle_commande.quantite
            
            # Remettre l'ancien stock
            ancien_medicament.quantite_stock += ancienne_quantite
            ancien_medicament.save()
            
            # Vérifier le nouveau stock
            if nouveau_medicament.quantite_stock == 0:
                messages.error(request, f'Stock vide pour {nouveau_medicament.nom}!')
                # Remettre l'ancien stock
                ancien_medicament.quantite_stock -= ancienne_quantite
                ancien_medicament.save()
            elif nouveau_medicament.quantite_stock >= nouvelle_quantite:
                nouveau_medicament.quantite_stock -= nouvelle_quantite
                nouveau_medicament.save()
                nouvelle_commande.save()
                messages.success(request, 'Commande modifiée!')
                return redirect('liste_commandes')
            else:
                # Remettre l'ancien stock car échec
                ancien_medicament.quantite_stock -= ancienne_quantite
                ancien_medicament.save()
                messages.error(request, f'Stock insuffisant! Disponible: {nouveau_medicament.quantite_stock}')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'listings/modifier_commande.html', {'form': form})

@login_required
def supprimer_commande(request, id):
    commande = get_object_or_404(Commande, id=id)
    if request.method == 'POST':
        commande.delete()
        return redirect('liste_commandes')
    return render(request, 'listings/supprimer_commande.html', {'commande': commande})

# === Authentification ===
def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'listings/connexion.html')


def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        # Vérifications de sécurité
        if password1 != password2:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
        elif len(password1) < 8:
            messages.error(request, 'Le mot de passe doit contenir au moins 8 caractères.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur existe déjà.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
        else:
            try:
                # Valider le mot de passe avec les règles Django
                validate_password(password1)
                user = User.objects.create_user(username=username, password=password1, email=email)
                messages.success(request, 'Compte créé avec succès! Vous pouvez maintenant vous connecter.')
                return redirect('connexion')
            except ValidationError as e:
                messages.error(request, ' '.join(e.messages))
    return render(request, 'listings/inscription.html')
def deconnexion(request):
    logout(request)
    return redirect('connexion')