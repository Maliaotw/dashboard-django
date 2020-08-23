# from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
# import django_filters
# from django.db import models
# from django import forms
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import User
# # from .models import UserLoginLog
#
# from app import models as app_models
#
# class FilteredListView(ListView):
#     filterset_class = None
#
#     def param_replace(self):
#         # 支持分頁器
#         data = self.request.GET.copy()
#         if self.page_kwarg in data.keys():
#             data.pop(self.page_kwarg)
#
#         return {k: v for k, v in data.items() if v}
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#
#         get = self.request.GET.copy()
#
#         self.filterset = self.filterset_class(get, queryset=queryset)
#         return self.filterset.qs.distinct()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filterset'] = self.filterset
#         context['search_field'] = self.param_replace()
#         return context
#
#
#
# class LoginListFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = UserLoginLog
#         fields = ['username']
#
#
#
# class CloudRecordListFilter(django_filters.FilterSet):
#
#     name = django_filters.CharFilter(
#         lookup_expr='icontains', label='名稱',method='filter_name')
#
#     def filter_name(self, queryset, name, value):
#         # print(queryset,name,value)
#         if queryset.filter(name__icontains=value):
#             return queryset.filter(name__icontains=value)
#         else:
#             return queryset.filter(instanceid__icontains=value)
#
#
#
#     class Meta:
#         model = app_models.CloudRecord
#         fields = ['name']