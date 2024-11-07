from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')


def Services(request):
    return render(request, 'Services.html')
def body(request):
    return render(request,'body.html')