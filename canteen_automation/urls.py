
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login),
    path('user_registration',views.user_registration),
    path('staff_registration',views.staff_registration),
    path('admin_home',views.admin_home),
]
