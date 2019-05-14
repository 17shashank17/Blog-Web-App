from django.shortcuts import render
from .models import PostAdd,UserSignup
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


def home(request):

    post_obj=PostAdd.objects.all()
    return render(request,"posts/home.html",{'post_obj':post_obj})

def details(request,pk):
    #url_refered=request.build_absolute_uri()
    #url_refered=url_refered.split('/')
    form1=PostAdd.objects.get(id=pk)
    print(form1.new_post)
    print(form1.post_image)
    user=User.objects.get(username=form1.delete_post)
    if request.user.is_authenticated:
        print("Yes")

    return render(request,"posts/details.html",{'form1':form1,'user':user})

def create_post(request):
    if request.method=="POST":
        post_heading=request.POST.get("title")
        post_to_add=request.POST.get("article")
        post_owner=request.POST.get("author")
        post_pic=request.FILES["pic"]
        obj=PostAdd()
        obj.new_post=post_to_add
        obj.heading=post_heading
        obj.author=post_owner
        obj.post_image=post_pic
        obj.save()
        return HttpResponseRedirect('/posts')
    return render(request,"posts/createpost.html",{})

def signup(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        conf_pass=request.POST.get("con_password")
        first=request.POST.get("first")
        last=request.POST.get("last")
        email=request.POST.get("email")
        profile_img=request.POST.get('profile_pic')
        print(username)
        if password != conf_pass or len(username)<8 or len(password)<8 or password=='' or first=='' or email=='':
            return render(request,'share/passwordnotmatch.html')
        try:
            user_check=User.objects.get(username=username)
            return render(request,'share/user_already_exist.html')
        except:
            user1=User()
            
            
            user1.username=username
            user1.set_password(str(password))
            user1.first_name=first
            user1.last_name=last
            user1.email=email
            user1.save()
            print(user1)
            user_pic=UserSignup.objects.get(delete_user=user1)
            user_pic.profile_image=profile_img
            user_pic.save()

            user=authenticate(username=username,password=password)
        

            login(request,user)

            return HttpResponseRedirect('/posts')
    else:
        return render(request,"posts/signup.html",{})

def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        request.session['username']=username
        user=authenticate(username=username,password=password)


        if user:
            login(request,user)
            #return render(request,'share/home.html')
            return HttpResponseRedirect('/posts/after_login')
        else:
            return render(request,"share/invalid_user.html")
    else:
        return render(request,"posts/login.html",{})

def after_login(request):
    #username=request.session['username']
    #user_obj=User.objects.get(username=username)
    content=PostAdd.objects.all()

    return render(request,'posts/after_login.html',{'content':content})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/posts')

def profile(request):
    print("In profiless")
    username=request.session['username']
    user_obj=User.objects.get(username=username)
    content=PostAdd.objects.filter(delete_post=user_obj)
    return render(request,'posts/profile.html',{'content':content,})

def details_after(request,pk):
    print("I am here")
    obj=PostAdd.objects.get(id=pk)
    return render(request,'posts/details_after.html',{'obj':obj})

#def delete(request):

