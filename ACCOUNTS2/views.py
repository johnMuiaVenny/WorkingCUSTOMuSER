from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import MyForm, DropForm
from .decorators import *
from django.contrib.auth.models import Group

# Create your views here.

@login_required(login_url='/ACCOUNTS2/Login')
@admin_only
def Home(request):
    return render(request, 'ACCOUNTS2/Home.html')



@login_required(login_url='/ACCOUNTS2/Login')
@allowed_users(allowed_roles=['admin', 'etc'])
def About(request):
    return render(request, 'ACCOUNTS2/About.html')



@unauthenticated_user
def Register(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name = 'customer')
            user.groups.add(group)
            messages.success(request, username + ' registered Successifully.' )
            return redirect('/ACCOUNTS2/Login')
    return render(request, 'ACCOUNTS2/Register.html', {'form':form})



@unauthenticated_user
def Login(request):
    # if request.user.is_authenticated:
    #     return redirect('/ACCOUNTS2/Home')
    # else:
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



#More knowledge on Decorators.
#@allowed_users(allowed_roles=['admin', 'etc'])
@Test(lists=['johnmuia'])
def UserPage(request):
    formf = DropForm()
    return render(request, 'ACCOUNTS2/UserPage.html', {'formf':formf})


