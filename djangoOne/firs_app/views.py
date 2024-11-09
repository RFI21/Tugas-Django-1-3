from django.shortcuts import render
from django.http import HttpResponse
from firs_app.models import Topic, Webpage, Accesrecord
from . import forms


# Create your views here.
def index (request):
    webpages_list = Accesrecord.objects.order_by('date')
    date_dict={'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)

def home (request):
    return render(request, 'basicapp/index.html')

def formview (request):
    form= forms.FormName()

    if request.method == 'POST':
        form= forms.FormName(request.POST)
        if form.is_valid():
            print("Validation Succes")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    return render(request, 'basicapp/form.html', {'form' : form})
