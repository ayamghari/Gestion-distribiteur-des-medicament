from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Fournisseur, Livreur, Medicament, Commande
from .forms import ClientForm, FournisseurForm, LivreurForm, MedicamentForm, CommandeForm
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
def liste_clients(request):
    query = request.GET.get('q', '')

    # TOUS les clients pour la liste déroulante
    tous_clients = Client.objects.all()

    # Base queryset
    clients = tous_clients

    # Filtre par nom (ou téléphone / adresse si tu veux)
    if query:
        clients = clients.filter(nom__icontains=query)

    return render(request, 'listings/liste_clients.html', {
        'clients': clients,          # pour le tableau
        'tous_clients': tous_clients, # pour la liste déroulante
        'query': query
    })

def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client ajouté avec succès!')
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
            messages.success(request, 'Client modifié avec succès!')
            return redirect('liste_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'listings/modifier_client.html', {'form': form})

@login_required
def supprimer_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client supprimé avec succès!')
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
            messages.success(request, 'Fournisseur ajouté avec succès!')
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
            messages.success(request, 'Fournisseur modifié avec succès!')
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'listings/modifier_fournisseur.html', {'form': form})

@login_required
def supprimer_fournisseur(request, id):
    fournisseur = get_object_or_404(Fournisseur, id=id)
    if request.method == 'POST':
        fournisseur.delete()
        messages.success(request, 'Fournisseur supprimé avec succès!')
        return redirect('liste_fournisseurs')
    return render(request, 'listings/supprimer_fournisseur.html', {'fournisseur': fournisseur})

# === Livreurs ===
@login_required
def liste_livreurs(request):
    livreurs = Livreur.objects.all()
    return render(request, 'listings/liste_livreurs.html', {'livreurs': livreurs})

@login_required
def ajouter_livreur(request):
    if request.method == 'POST':
        form = LivreurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livreur ajouté avec succès!')
            return redirect('liste_livreurs')
    else:
        form = LivreurForm()
    return render(request, 'listings/ajouter_livreur.html', {'form': form})

@login_required
def modifier_livreur(request, id):
    livreur = get_object_or_404(Livreur, id=id)
    if request.method == 'POST':
        form = LivreurForm(request.POST, instance=livreur)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livreur modifié avec succès!')
            return redirect('liste_livreurs')
    else:
        form = LivreurForm(instance=livreur)
    return render(request, 'listings/modifier_livreur.html', {'form': form})

@login_required
def supprimer_livreur(request, id):
    livreur = get_object_or_404(Livreur, id=id)
    if request.method == 'POST':
        livreur.delete()
        messages.success(request, 'Livreur supprimé avec succès!')
        return redirect('liste_livreurs')
    return render(request, 'listings/supprimer_livreur.html', {'livreur': livreur})

# === Médicaments ===
@login_required
def liste_medicaments(request):
    query = request.GET.get('q', '')
    filtre_stock = request.GET.get('stock', '')
    
    # Obtenir TOUS les médicaments pour la liste déroulante
    tous_medicaments = Medicament.objects.all()
    medicaments = tous_medicaments
    
    # Recherche par nom
    if query:
        medicaments = medicaments.filter(nom__icontains=query)
    
    # Filtre par stock
    if filtre_stock == 'vide':
        medicaments = medicaments.filter(quantite_stock=0)
    elif filtre_stock == 'faible':
        medicaments = medicaments.filter(quantite_stock__lt=10, quantite_stock__gt=0)
    
    return render(request, 'listings/liste_medicaments.html', {
        'medicaments': medicaments,
        'tous_medicaments': tous_medicaments,
        'query': query,
        'filtre_stock': filtre_stock
    })
@login_required
def ajouter_medicament(request):
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médicament ajouté avec succès!')
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
            messages.success(request, 'Médicament modifié avec succès!')
            return redirect('liste_medicaments')
    else:
        form = MedicamentForm(instance=medicament)
    return render(request, 'listings/modifier_medicament.html', {'form': form})

@login_required
def supprimer_medicament(request, id):
    medicament = get_object_or_404(Medicament, id=id)
    if request.method == 'POST':
        medicament.delete()
        messages.success(request, 'Médicament supprimé avec succès!')
        return redirect('liste_medicaments')
    return render(request, 'listings/supprimer_medicament.html', {'medicament': medicament})

# === Commandes ===
@login_required
def liste_commandes(request):
    statut_filtre = request.GET.get('statut', '')
    query_client = request.GET.get('client', '')

    tous_clients = Client.objects.all()
    commandes = Commande.objects.all()
    livreurs = Livreur.objects.all()  # 👈 IMPORTANT

    if query_client:
        commandes = commandes.filter(client__nom__icontains=query_client)

    if statut_filtre:
        commandes = commandes.filter(statut=statut_filtre)

    return render(request, 'listings/liste_commandes.html', {
        'commandes': commandes,
        'tous_clients': tous_clients,
        'statut_filtre': statut_filtre,
        'query_client': query_client,
        'livreurs': livreurs,  # 👈 IMPORTANT
    })
@login_required
def affecter_livreur(request, id):
    if request.method == 'POST':
        commande = get_object_or_404(Commande, id=id)
        livreur_id = request.POST.get('livreur_id')
        
        if livreur_id:
            livreur = get_object_or_404(Livreur, id=livreur_id)
            commande.livreur = livreur
        else:
            commande.livreur = None
        
        commande.save()
        messages.success(request, 'Livreur affecté avec succès !')
        
    return redirect('liste_commandes')
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
                messages.success(request, 'Commande créée avec succès!')
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
            ancien_medicament.quantite_stock += ancienne_quantite
            ancien_medicament.save()
            if nouveau_medicament.quantite_stock == 0:
                messages.error(request, f'Stock vide pour {nouveau_medicament.nom}!')
                ancien_medicament.quantite_stock -= ancienne_quantite
                ancien_medicament.save()
            elif nouveau_medicament.quantite_stock >= nouvelle_quantite:
                nouveau_medicament.quantite_stock -= nouvelle_quantite
                nouveau_medicament.save()
                nouvelle_commande.save()
                messages.success(request, 'Commande modifiée avec succès!')
                return redirect('liste_commandes')
            else:
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
        messages.success(request, 'Commande supprimée avec succès!')
        return redirect('liste_commandes')
    return render(request, 'listings/supprimer_commande.html', {'commande': commande})
@login_required
def modifier_commande_client(request, id):
    commande = get_object_or_404(
        Commande,
        id=id,
        client__user=request.user
    )

    if request.method == 'POST':
        nouvelle_quantite = int(request.POST.get('quantite', 0))
        ancienne_quantite = commande.quantite
        medicament = commande.medicament

        difference = nouvelle_quantite - ancienne_quantite

        if nouvelle_quantite <= 0:
            messages.error(request, "Quantité invalide")
        elif medicament.quantite_stock < difference:
            messages.error(request, "Stock insuffisant")
        else:
            medicament.quantite_stock -= difference
            medicament.save()

            commande.quantite = nouvelle_quantite
            commande.save()

            messages.success(request, "Commande modifiée avec succès")
            return redirect('espace_client')

    return render(request, 'client/modifier_commande.html', {
        'commande': commande
    })
  
@login_required
def supprimer_commande_client(request, id):
    client = Client.objects.get(user=request.user)
    commande = get_object_or_404(Commande, id=id, client=client)

    if commande.statut != 'en_cours':
        messages.error(request, "Impossible de supprimer cette commande")
        return redirect('espace_client')

    medicament = commande.medicament
    medicament.quantite_stock += commande.quantite
    medicament.save()

    commande.delete()
    messages.success(request, "Commande supprimée")
    return redirect('espace_client')

@login_required
def changer_statut_commande(request, id):
    if request.method == 'POST':
        commande = get_object_or_404(Commande, id=id)
        commande.statut = request.POST.get('statut')
        commande.save()
        messages.success(request, 'Statut changé avec succès!')
    return redirect('liste_commandes')

@login_required
def espace_client(request):
    client = Client.objects.get(user=request.user)
    medicaments = Medicament.objects.all()
    commandes = Commande.objects.filter(client=client)

    if request.method == 'POST':

        # ===== MODIFIER INFOS CLIENT =====
        if 'update_client' in request.POST:
            client.nom = request.POST.get('nom', client.nom)
            client.telephone = request.POST.get('telephone', client.telephone)
            client.adresse = request.POST.get('adresse', client.adresse)
            client.save()
            messages.success(request, "Informations mises à jour avec succès")

        # ===== COMMANDER =====
        elif 'commander' in request.POST:
            medicament_id = request.POST.get('medicament')
            quantite = int(request.POST.get('quantite', 0))

            medicament = Medicament.objects.get(id=medicament_id)

            if quantite <= 0:
                messages.error(request, "Quantité invalide")
            elif medicament.quantite_stock < quantite:
                messages.error(request, "Stock insuffisant")
            else:
                medicament.quantite_stock -= quantite
                medicament.save()

                Commande.objects.create(
                    client=client,
                    medicament=medicament,
                    quantite=quantite,
                    statut='en_cours'
                )

                messages.success(request, "Commande enregistrée avec succès")

    return render(request, 'client/espace_client.html', {
        'client': client,
        'medicaments': medicaments,
        'commandes': commandes
    })
@login_required
def affecter_livreur(request, id):
    commande = get_object_or_404(Commande, id=id)

    if request.method == "POST":
        livreur_id = request.POST.get("livreur")

        if livreur_id:
            livreur = get_object_or_404(Livreur, id=livreur_id)
            commande.livreur = livreur
        else:
            commande.livreur = None

        commande.save()
        messages.success(request, "Livreur affecté avec succès")

    return redirect("liste_commandes")

# === Authentification ===
def connexion(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)
            if user.is_staff:
                return redirect('accueil')
            else:
                return redirect('espace_client')
        else:
            messages.error(request, 'Identifiants incorrects')

    return render(request, 'listings/connexion.html')


def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 != password2:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
        else:
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                is_staff=False
            )

            Client.objects.create(
                user=user,
                nom=username,
                telephone=''
            )

            messages.success(request, 'Compte créé avec succès.')
            return redirect('connexion')

    return render(request, 'listings/inscription.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')