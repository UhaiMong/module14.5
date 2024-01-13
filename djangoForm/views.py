from djangoForm.forms import CollectionForm
from django.shortcuts import render
from . forms import practiceForms
# Create your views here.


def home(request):
    return render(request, 'home.html')


def myForm(request):
    if request.method == 'POST':
        form = practiceForms(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./djangoForm/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'myForm.html', {'form': form})
    else:
        form = practiceForms()
    return render(request, 'myForm.html', {'form': form})


def modelForm(request):
    if request.method == 'POST':
        data = CollectionForm(request.POST)
        if data.is_valid():
            data.save()
            print(data.cleaned_data)
    else:
        data = CollectionForm()
    return render(request, 'modelForm.html', {'data': data})
