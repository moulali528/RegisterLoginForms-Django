from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def home_page(request):
    if request.method == "POST":
        #Get the user details from Form
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticate the user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You have been logged in successfully...')
            #return render(request, 'home_page.html')
            return render(request, 'home_page.html', {})
        else:
            messages.error(request, 'Issue occured while login !!')
            return redirect('home')
    else:
        #messages.error(request, 'Issue occured while logged in, Please try again ...')
        return render(request, 'home_page.html', {})
        #return redirect(request, 'home')
    
def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out successfully...')
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			#username = form.cleaned_data['username']
			#password = form.cleaned_data['password1']
			#user = authenticate(username=username, password=password)
			#login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register_page.html', {'form':form})

	return render(request, 'register_page.html', {'form':form})