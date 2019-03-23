from django.shortcuts import render
from .models import PostAdd
from django.http import HttpResponseRedirect

class Link:

    def get_random_link(self):
        b=string.ascii_letters
        q=random.choice(b)
        r=random.choice(b)
        s=random.randint(10,100)
        w=random.choice(b)
        t=random.choice(b)
        c=q+r+w+t+str(s)
        c=c+'/'
        return c

def home(request):

    post_obj=PostAdd.objects.all()
    return render(request,"posts/home.html",{'post_obj':post_obj})

def details(request):
    url_refered=request.build_absolute_uri()
    url_refered=url_refered.split('/')
    form1=PostAdd.objects.get(random_link=url_refered[4])
    return render(request,"/posts/details.html",{'form1':form1})

def create_post(request):
    if request.method=="POST":
        l=Link()
        post_heading=request.POST.get("title")
        post_to_add=request.POST.get("article")
        post_owner=request.POST.get("author")
        obj=PostAdd()
        obj.new_post=post_to_add
        obj.heading=post_heading
        obj.author=post_owner
        rand_link=l.get_random_link()
        obj.random_link=rand_link
        obj.save()
        return HttpResponseRedirect(rand_link)
    return render(request,"posts/createpost.html",{})
