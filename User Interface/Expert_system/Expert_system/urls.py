from django.contrib import admin
from django.urls import path
# from django.conf.urls import patterns, url
from predict import views
from django.urls import include, re_path
from django.contrib.auth import views as auth_view

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'Homepage',views.index,name='Homepage'),
    re_path(r'predictModel',views.predictModel,name='predictModel'),
    re_path(r'viewdatabase',views.viewDatabase,name='viewdatabase'),
    re_path(r'updateDatabase',views.updateDatabase,name='updateDatabase'),
    re_path(r'^$', views.home, name='home'),
    re_path(r'register/', views.register, name='register'),
    re_path(r'profile/', views.profile, name='profile'),
    re_path(r'login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    re_path(r'logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
]
