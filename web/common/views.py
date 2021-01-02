from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from app import models


class DashBoardView(View):

    def get(self, request):
        counts = {
            'asset': models.Asset.objects.all().count(),
            'server': models.Asset.objects.filter(category__name='服務器').count(),
            'netware': models.Asset.objects.filter(category__name='網路設備').count(),
            'host': models.Asset.objects.filter(category__name='虛擬機').count(),

        }

        return render(request, 'dashboard.html', locals())


class DashRackView(APIView):

    def get(self, request):
        busline_obj = models.Busline.objects.all()

        data = {'label':[],'data':[]}
        for busline in busline_obj:
            data['data'].append(models.Asset.objects.filter(busline=busline).count())
            data['label'].append(busline.name)

        # numbers = list(range(30))
        #
        # data = {
        #     'label': ['機櫃A', '機櫃B', '機櫃C'],
        #     'data': [random.choice(numbers), random.choice(numbers), random.choice(numbers)]
        # }
        return Response(data)


class DashAssetView(APIView):

    def recent_seven_days(self):
        import datetime
        from django.utils import timezone
        today = timezone.now().date()
        # lists = []
        for i in range(7):
            # lists.append(date.strftime('%Y-%m-%d'))
            yield today - datetime.timedelta(days=i)

    def get(self, request):
        # print('recent_seven_days', self.recent_seven_days())
        random_range_num = list(range(20))
        list_week_day = list(self.recent_seven_days())
        list_week_day.reverse()

        server_list = []
        netware_list = []
        vm_list = []

        for day in list_week_day:
            server_list.append(random.choice(random_range_num))
            netware_list.append(random.choice(random_range_num))
            vm_list.append(random.choice(random_range_num))

        data = {
            'label': [i.strftime('%Y-%m-%d') for i in list_week_day],
            'server_list': server_list,
            'netware_list': netware_list,
            'vm_list': vm_list,
        }

        return Response(data)
