from django.http import HttpResponse
from django.shortcuts import render, redirect



def home(request):
    # if request.method == "POST":
    #     form  = ContactForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         message = form.cleaned_data['message']
    #         form.save()
    #         return redirect("thank-you")
        
    # else:
    #     form = ContactForm()
        
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def elements(request):
    return render(request, "elements.html")


def gallery(request):
    return render(request, "gallery.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def news(request):
    return render(request, "news.html")


def staff(request):
    return render(request, "staff.html")