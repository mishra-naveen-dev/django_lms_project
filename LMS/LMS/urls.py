
from django.contrib import admin
from django.urls import path,include
from .import views,user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),

    path('', views.HOME, name='home'),
    path('single/course', views.SINGLE_COURSE, name='single_cousre'),
    path('contact',views.CONTACT_US,name='contact_us'),
    path('about',views.ABOUT_US,name='about_us'),

    path('accounts/register', user_login.REGISTER, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin',user_login.Do_LOGIN,name='doLogin'),
]
