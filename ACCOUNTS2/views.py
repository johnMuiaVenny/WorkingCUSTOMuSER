from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import MyForm

# Create your views here.

@login_required(login_url='/ACCOUNTS2/Login')
def Home(request):
    return render(request, 'ACCOUNTS2/Home.html')

@login_required(login_url='/ACCOUNTS2/Login')
def About(request):
    return render(request, 'ACCOUNTS2/About.html')



def Register(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' registered Successifully.' )
            return redirect('/ACCOUNTS2/Login')
    return render(request, 'ACCOUNTS2/Register.html', {'form':form})




def Login(request):
    if request.method == 'POST':
        next = request.GET.get('next') #Go to the Intended page.
        Username = request.POST['username']
        Pass1 = request.POST['password1']
        user = auth.authenticate(username=Username, password=Pass1)
        if user is not None:
            auth.login(request, user)
            if next:
                return redirect(next)
            return redirect('/ACCOUNTS2/Home')
        else:
            messages.error(request, 'Invalid Credentials!!')
            return redirect('/ACCOUNTS2/Login')
    return render(request, 'ACCOUNTS2/Login.html')


def Logout(request):
    auth.logout(request)
    return HttpResponse('LOGED OUT.')
