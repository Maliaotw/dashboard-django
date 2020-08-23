"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
# from authentication.views import UserLoginView, UserLogoutView
from django.contrib.auth.decorators import login_required, permission_required
# from app.views import acc_login, acc_logout
from authentication.views import UserLoginView,UserLogoutView

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # login / logout
    path('login/', UserLoginView.as_view(), name="login"),
    # path('login/', acc_login, name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    # path('logout/', acc_logout, name="logout"),

    # App
    path('', include('app.urls')),
    path('', include('authentication.urls')),

]
