from django.http import Http404
from django.shortcuts import render,redirect
from .forms import SignUpForm,UserLoginForm
from django.contrib import messages,auth
# LOGIN VIEW ENDPOINT

def login(request):

    context={}

    if request.method=='POST':

        user_form=UserLoginForm(request.POST)

        if user_form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))

            if user:
                auth.login(request,user)
                messages.success(request, "You have successfully logged in")
            else:
                messages.error(request,"Your input data is not correct")

        return redirect('home')    
    
    else:
        user_form=UserLoginForm()
        context['user_form']=user_form
    return render(request, 'login.html',context)


def register(request):
    context={}
    if request.method=='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password1'))
            
            if user:
                auth.login(request, user)
            messages.success(request,"User Saved")
            return redirect('home')
        else:
            messages.error(request,"Error in form")
            return redirect('register')
    else:
        form=SignUpForm()
    
    context['form']=form
    return render(request, 'register.html',context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')