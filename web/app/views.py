from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from . import models
from . import tasks
from . import filters
from . import forms


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve

import logging


# # Create your views here.



# --- 登入/登出 ---

def acc_login(request):
    error_msg = ""

    next = request.GET.get('next', '')

    if request.method == 'GET':

        # 判斷是否已登入
        resolve_obj = resolve(request.GET.get('next'))

        # print(request)

        if request.user.is_authenticated:
            return redirect(next)

    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(next)

        else:
            error_msg = "使用者或密碼有誤!!"

        print(user, username, password)

    return render(request, 'login.html', locals())


def acc_logout(request):
    logout(request)
    # print("logout")
    return redirect('asset-list')


# Asset
class AssetListView(filters.FilteredListView):
    model = models.Asset
    paginate_by = 10
    filterset_class = filters.AssetListFilter
    template_name = 'app/asset_list.html'


    def get_context_data(self):

        if self.request.GET.get('contacts'):
            self.paginate_by = int(self.request.GET.get('contacts',10))
        context = super().get_context_data()
        context.update({
            'page_list':[10,20,50,100]
        })
        # print(context)
        return context
