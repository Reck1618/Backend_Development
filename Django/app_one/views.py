from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicationForm

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
    context = {'form': form}
    return render(request, 'form2.html', context)

def get_index(request):
    return HttpResponse("Form Submitted")
