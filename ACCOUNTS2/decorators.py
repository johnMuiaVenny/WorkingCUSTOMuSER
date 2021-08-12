from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/ACCOUNTS2/Home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("You are not allowed to view this page.")

        return wrapper_func
    return decorator   



def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('/ACCOUNTS2/UserPage')
        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func 


def Test(lists=[]):
    def muia(view_func):
        def working_func(request, *args, **kwargs):
            if lists[0] == 'johnmuia':
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("CONDITION FAILED.")
        return working_func
    return muia
        