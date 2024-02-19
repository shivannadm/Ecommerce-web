from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    return render(request,"signup.html")

def handlelogin(request):
    return render(request,"login.html")

def handlelogout(request):
    return redirect('/auth/login')
