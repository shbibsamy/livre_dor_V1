from django.shortcuts import render
from . import forms
from . import models

def home(request):
    if request.method == 'POST':
        form = forms.FormulaireCommentaire(request.POST)
        if form.is_valid():
            cmt = models.Commentaire()
            cmt.__setattr__('email', form.cleaned_data['email'])
            cmt.__setattr__('contenu', form.cleaned_data['contenu'])
            cmt.save()
            message = 'Merci !'
            context = {'formulaire' : forms.FormulaireCommentaire, 'message' : message}
    else :
        message = 'Veuillez laisser votre commentaire.'
    data = models.Commentaire.objects.all().values
    context = {'formulaire' : forms.FormulaireCommentaire, 'message' : message, 'data' : data}
    return render(request, 'index.html', context)