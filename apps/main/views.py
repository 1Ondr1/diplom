from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')