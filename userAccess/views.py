from django.shortcuts import render
from django.http import HttpResponse
#from .models import user
from .forms import userLogin, userSignup, userSignup_profile
from django.contrib.auth import login
from django.contrib.sessions.models import Session 
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from shoppingCart.models import Profile
from django.contrib.auth.hashers import make_password


# Create your views here.
def user_home(request):
    form = userLogin()
    return render(request,"userhome.html",{'form':form, 'messages':''})

def user_signup(request):
    if request.method == "POST":
        user_form = userSignup(request.POST)
        phone = request.POST['phone']
        address = request.POST['address']
        pincode = request.POST['pincode']
        if user_form.is_valid() :
            user = user_form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            auth.login(request,user)
            userdata = User.objects.all()
            for userinfo in userdata:
                if userinfo.username == user.username:
                    user_id=user.id
            update_data = Profile.objects.get(pk = user_id)
            update_data.address=address
            update_data.phone=phone
            update_data.pincode=pincode
            update_data.save()
            return redirect('/')

        # else:
        #     return HttpResponse(" SIGNUP FAILED")

    else:
        user_form = userSignup()
        profile_form = userSignup_profile()
        return render(request,"user_signup.html",{'form':user_form, 'profile_form':profile_form})
    profile_form = userSignup_profile()
    profile_form.fields["phone"].initial=phone
    profile_form.fields["address"].initial=address
    profile_form.fields["pincode"].initial=pincode
    return render(request, "user_signup.html", {'form':user_form, 'profile_form':profile_form})

def user_logout(request):
    auth.logout(request)
    return redirect('/')

def user_login(request):
    
    if request.method == "POST":
        nexturl = request.POST['next'].strip(' ')
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['count']=1
            if nexturl != '':
                return redirect(nexturl)
            else:
                return redirect('/')
    form = userLogin()
    form.fields["username"].initial=username
    return render(request, "userhome.html" , {'form':form, 'messages':"Incorrect Username or Password"} )