from django import forms
from .models import Commentaire

class FormulaireCommentaire(forms.Form):
    email = forms.EmailField(label='Votre email ')
    contenu = forms.CharField(label='Votre commentaire ', widget=forms.Textarea, help_text='(Maximum de 750 caractères)')
    
    class Meta:
        model = Commentaire
        fields = ['email', 'contenu']