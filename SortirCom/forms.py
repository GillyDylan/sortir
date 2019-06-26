from django import forms
from django.core.validators import RegexValidator
from SortirCom.models import Site, Lieu, Ville


class ParticipantForm(forms.Form):
    pseudo = forms.CharField(min_length=3, max_length=50, required=True, label='Pseudo :')
    email = forms.EmailField(max_length=100, required=True, label='E-mail :')
    nom = forms.CharField(min_length=2, max_length=50, required=True, label='Nom :')
    prenom = forms.CharField(min_length=2, max_length=50, required=True, label='Prenom :')
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=100, required=True, label='Mot de Passe :')
    confirmPassword = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=100, required=True, label='Confirmer mdp :')
    telephone = forms.CharField(validators=[RegexValidator(r'^\d{10}$')], min_length=10, max_length=10, required=True, label='Téléphone :')
    site = forms.ModelChoiceField(queryset=Site, empty_label=None, required=True, label='Site rataché :')
    administrateur = forms.BooleanField(required=False, label='Est administrateur :')
    actif = forms.BooleanField(required=False, label='Est actif :')


class SortieForm(forms.Form):
    nom = forms.CharField(min_length=2, max_length=50, required=True, label='Nom Sortie :')
    dateHeureDebut = forms.DateTimeField(required=True, label='Date début de l\'évenement :')
    dateHeureFin = forms.DateTimeField(required=True, label='Date fin de l\'évenement :')
    dateLimiteInscription = forms.DateField(required=True, label='Date limite d\'inscription :')
    nbInscriptionMax = forms.IntegerField(min_value=1, required=True, label='Participants maximum :')
    infosSortie = forms.CharField(widget=forms.Textarea, required=True, label='infos :')
    lieu = forms.ModelChoiceField(queryset=Lieu, empty_label=None, required=True, label='Lieu :')


class SiteForm(forms.Form):
    nom = forms.CharField(min_length=2, max_length=50, required=True, label=None)


class VilleForm(forms.Form):
    nom = forms.CharField(min_length=2, max_length=50, required=True, label=None)
    codePostal = forms.CharField(min_length=5, max_length=5, validators=[RegexValidator(r'^\d{5}$')])


class LieuForm(forms.Form):
    nom = forms.CharField(min_length=2, max_length=50, required=True, label='Nom lieu :')
    rue = forms.CharField(min_length=2, max_length=50, required=True, label='rue lieu :')
    latitude = forms.FloatField(required=True, label='latitude :')
    longitude = forms.FloatField(required=True, label='longitude :')
    ville = forms.ModelChoiceField(queryset=Ville, required=True, label='Ville :')


class ConnexionFor(forms.Form):
    pseudo = forms.CharField(min_length=3, max_length=50, required=True, label='Pseudo :')
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=100, required=True, label='Mot de Passe :')
    administrateur = forms.BooleanField(required=False, label='Se souvenir de moi ?')
