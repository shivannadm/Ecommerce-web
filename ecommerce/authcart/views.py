from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    print("I'm running")
    return render(request,"signup.html")

def handlelogin(request):
    return render(request,"login.html")

def handlelogout(request):
    return redirect('/auth/login')
