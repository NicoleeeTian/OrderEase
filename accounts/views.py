from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserForm
from .models import User

# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # is_valid() check based on model if email and username are unique
            # Create the usering using the form
            # is_valid() finction in Django form is used to perform validation for each filed on the form.
            # user = form.save(commit=False) # ready to save but not yet
            # user.role = User.CUSTOMER
            # # hash password before save
            # password = form.cleaned_data['password']
            # user.set_password(password)

            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role = User.CUSTOMER
            user.save()
            print('user is saved')
            messages.success(request,'Your account has been successfully registered!')
            # success is the tag name, it can be error, warining
            return redirect('registerUser')
        else:
            # is the form is not valid
            print('invalid form', form.errors)
    else:
        # GET 
        form = UserForm()
    
    context = {
        'form': form,
    }
    return render(request,'accounts/registerUser.html',context)