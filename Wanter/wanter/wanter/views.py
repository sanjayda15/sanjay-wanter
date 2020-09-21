from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,get_user_model
from django.http import HttpResponse,JsonResponse

from .forms import ContactForm

def home_page(request):
    #print(request.session.get('first_name','unknown'))
    #request.session['first_name']
    context = {"title": 'Wanter ',
               "describe": "This is a fashion e-Commerce Website. "}
    if request.user.is_authenticated:
        context['premium_content'] = 'Yeaahgotit'
    return render(request, "index.html", context)

def practice_page(request):
    return render(request,'practice.html',{})

def about_page(request):
    context = {'title' : 'About',
               'describe': "welcome to about page"}
    return render(request, "about_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {'title' : 'Contact',
               'describe': "Welcome to Contact Page..",
               'form':contact_form}
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('Name'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, "contact_page.html", context)
