from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomerUserCreationForm
from django.contrib.auth import authenticate, login

@login_required
def usuario(request):
    return render(request, "nivel.html")

def exit(request):
    logout(request)
    return redirect("home")

def register(request):
    data={
        'form': CustomerUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomerUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user= authenticate(username=user_creation_form.cleaned_data['username'], password= user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('home')
        
    return render(request, "registration/register.html", data)