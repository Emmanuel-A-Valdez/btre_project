from django.shortcuts import redirect, render


def register(request):

    context = {

    }
    if request.method == 'POST':
        # Register User
        pass
    else:
        return render(request, 'accounts/register.html', context)


def login(request):
    
    context = {
        
    }
    if request.method == 'POST':
        # Login User
        pass
    else:
        return render(request, 'accounts/login.html', context)


def logout(request):
    
    return redirect('index')


def dashboard(request):
    
    context = {

    }
    return render(request, 'accounts/dashboard.html', context)



