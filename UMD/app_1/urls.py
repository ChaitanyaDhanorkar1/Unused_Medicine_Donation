"""UMD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_function),
    path('medicine_donation',views.donation_function),
    path('medicine_request',views.request_function),
    path('user_feedback',views.feedback_function),
    path('monetory_donation',views.monetory_function),
    path('show',views.show),
    path('send',views.send),
    path('delete',views.delete),
    path('adminedit',views.adminedit),
    path('RecordEdited',views.RecordEdited),
    path('login',views.login_user),
    path('otpfunc',views.otpfunc),
    path('register',views.register),
    path('donations',views.donations),
    path('approvedonate',views.approvedonate),
    path('rejectdonate',views.rejectdonate),
    path('adminlogin',views.adminlogin),
    path('requests',views.requests),
    path('approverequest',views.approverequest),
    path('rejectrequest',views.rejectrequest),
    path('userlogout',views.userlogout),
    path('adminlogout',views.adminlogout),
    path('stocks',views.stocks),
    path('profile',views.profile),
    path('adminprofile',views.adminprofile),
    # path('test',views.test)
    path('dispose',views.dispose)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
