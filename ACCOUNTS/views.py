from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def Home(request):
    return HttpResponse("JOHN MUIA<br>MAGGY IS A FORTH YEAR STUDENT.")

def Register(request):
    if request.method == 'POST':
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        Username = request.POST['username']
        Email = request.POST['email']
        Pass1 = request.POST['password1']
        Pass2 = request.POST['password2']

        if len(Pass1)>=8 and len(Pass1)<=16:
            if Pass1==Pass2:
                if User.objects.filter(username = Username).exists():
                    messages.error(request, 'Username taken.!! Try another.')
                    return redirect('/')
                elif User.objects.filter(email = Email).exists():
                    messages.error(request, 'Email taken.!! Try another.')
                    return redirect('/')
                else:
                    user = User.objects.create_user(first_name=Fname, last_name=Lname, username=Username, email=Email, password=Pass1)
                    user.save()
                    user = request.POST['username']
                    messages.success(request, user + ' created successifully.')
                    return redirect('/')
            else:
                messages.error(request, 'Password mismatch.')
                return redirect('/')
        else:
            messages.error(request, 'Password must be between 8-16 characters long!!')
            return redirect('/')
    return render(request, 'ACCOUNTS/Register.html')

#ppppppppppppppppppppppppppppppppppppppppppppppppppppppp

def Login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Pass1 = request.POST['password1']

        user = auth.authenticate(username=Username, password=Pass1)
        if user is not None:
            auth.login(request, user)
            user = request.POST['username']
            messages.success(request, user + ' Loged in successifully.')
            return redirect('/Login')
        else:
            messages.error(request, 'Invalid Credentials!!')
            return redirect('/Login')
    return render(request, 'ACCOUNTS/Login.html')


#ppppppppppppppppppppppppppppppppppppppppppppppppppppppp

def Logout(request):
    auth.logout(request)
    return HttpResponse("LOGED OUT.")