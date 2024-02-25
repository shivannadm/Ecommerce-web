from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# from django.views.generic import View
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
# from .utils import TokenGenerator,generate_token
# from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.utils.http import urlsafe_base64_decode
# from django.utils.encoding import force_str
# from django.contrib.auth.tokens import PasswordResetTokenGenerator 
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')                   
        
        try:
            if User.objects.get(username=email):
                return HttpResponse("Email already exist")

        except Exception as identifier:
            pass

        user = User.objects.create_user(email,email,password)
        user.save()
        return HttpResponse("User created",email)
    return render(request,"signup.html")


def handlelogin(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')

        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/login')

    return render(request,'login.html')  






def handlelogout(request):
    # logout(request)
    # messages.info(request,"Logout Success")
    return redirect('/auth/login')


# class RequestResetEmailView(View):
#     def get(self,request):
#         return render(request,'request-reset-email.html')
    
#     def post(self,request):
#         email=request.POST['email']
#         user=User.objects.filter(email=email)

#         if user.exists():
#             # current_site=get_current_site(request)
#             email_subject='[Reset Your Password]'
#             message=render_to_string('reset-user-password.html',{
#                 'domain':'127.0.0.1:8000',
#                 'uid':urlsafe_base64_encode(force_bytes(user[0].pk)),
#                 'token':PasswordResetTokenGenerator().make_token(user[0])
#             })

            # email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
            # email_message.send()