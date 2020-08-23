
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from .views import LoginListView



urlpatterns = [
    path('logs/', login_required(LoginListView.as_view()), name='login-list'),

]

