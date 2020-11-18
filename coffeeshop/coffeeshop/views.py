from django.template import loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib.auth import login

from .models import User, CoffeeType, Coffee

from . import forms
POST = "POST"

def home(request:HttpRequest) -> HttpResponse:
    template = loader.get_template('coffeeshop/home.html')
    
    context = {}
    return HttpResponse(template.render(context, request))


def signup_old(request:HttpRequest) -> HttpResponse:
    if request.method == POST:
        #proces the form data
        form = forms.NameForm(request.POST)

        if form.is_valid():
            # validate the data
            # ...
            # redirect to a new url
            form.save()
            return HttpResponseRedirect('thanks')
    else:
        # create a blank form
        form = forms.NameForm()
    
    # template = loader.get_template('coffeeshop/signup.html')
    # context = {
    #     'form':form

    # }
    # return HttpResponse(template.render(context,request))
    return render(request,'coffeeshop/signup.html',{'form':form})

def thanks(request:HttpResponse) -> HttpResponse:
    context = {}
    return render(request,'coffeeshop/thanks.html',context)


def signup(request:HttpRequest) -> HttpResponse:
    if request.method == POST:
        form = forms.Signup(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('details')
    else:
        form = forms.Signup(initial={'email':'@gmail.com'})
    
    return render(request, 'coffeeshop/signup.html', {'form':form})


def details(request:HttpRequest) -> HttpResponse:
    if request.method == POST:
        form = forms.UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thanks')
    else:
        form = forms.UserDetailsForm(initial={'username':request.user.username, 'email':request.user.email})
    
    return render(request, 'coffeeshop/signup.html', {'form':form})


def place_order(request:HttpRequest) -> HttpResponse:
    OrderFormSet = modelformset_factory(Coffee, fields=['name', 'size', 'quantity'],max_num=4, extra=2)
    if request.method == POST:
        order_formset = OrderFormSet(request.POST)
        if order_formset.is_valid():
            order_formset.save()
            return redirect('/')
    else:
        order_formset = OrderFormSet()
        return render(request, 'coffeeshop/order.html', {'formset': order_formset})