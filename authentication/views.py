from django.http import Http404
from django.shortcuts import render,redirect
from .forms import SignUpForm,UserLoginForm
from django.contrib import messages,auth

#api related import
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import  RegisterSerializer


from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


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


#api views 

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        auth.login(request, user)
        return super(LoginAPI, self).post(request, format=None)