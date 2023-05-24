from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicationForm, LogForm

# Create your views here.
def home(request):
    content = "<html><body><h1>Welcome to my Home Page</h1></body></html>"
    return HttpResponse(content)

def demo(request):
    path = request.path
    method = request.method
    content = f"<html><body><h1>Welcome to my Demo Page</h1><p>Path: {path}</p><p>Method: {method}</p></body></html>"
    return HttpResponse(content)

def show_form(request):
    return render(request, 'form.html')

def get_form(request):
    if request.method == "POST":
        UserID = request.POST['id']
        name = request.POST['name']
    return HttpResponse(f"Name: {name} <br> ID: {UserID}")

def dish(request, name):
    dishes = {
        'tofu': 'You a soy boy',
        'cheese': 'french? lol',
        'paneer': 'Finally! something healthy',
    }

    content = f"<html><body><h1>{name}</h1><h2>{dishes[name]}</h2></body></html>"
    return HttpResponse(content)
        
def index(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            field = form.cleaned_data['field']
            return HttpResponse(f"Form Submitted! <br> Name: {name} <br> Address: {address} <br> Field: {field}")
    context = {'form': form}
    return render(request, 'form2.html', context)


def logger_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form Submitted!")
    context = {'form': form}
    return render(request, 'logger.html', context)

