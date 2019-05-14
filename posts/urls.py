
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^create_post/',views.create_post,name="create_post"),
    url(r'^(?P<pk>\d+)/$', views.details, name='details'),
    url(r'^signup/',views.signup,name="signup"),
    url(r'^login_user/',views.login_user,name="login_user"),
    #url(r'^delete/',views.delete,name="delete"),
    url(r'^after_login',views.after_login,name="after_login"),
    url(r'^logout_user',views.logout_user,name="logout_user"),
    url(r'^profile\/(?P<pk>\d+)/$',views.details_after,name="details_after"),
    url(r'^profile',views.profile,name='profile'),
    
]