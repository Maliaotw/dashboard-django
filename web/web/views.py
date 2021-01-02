from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
import random


class DashBoardView(View):

    def get(self, request):
        counts = {
            'asset': 3,
            'server': 5,
            'netware': 7,
            'host': 1,

        }

        return render(request, 'dashboard.html', locals())


class DashRackView(APIView):

    def get(self, request):
        # rack_obj = asset_models.Rack.objects.all()
        #
        #
        #
        # data = {'label':[],'data':[]}
        # for r in rack_obj:
        #     data['data'].append(sum([i.size for i in r.asset_set.all()]))
        #     data['label'].append(r.name)

        numbers = list(range(30))

        data = {
            'label': ['機櫃A', '機櫃B', '機櫃C'],
            'data': [random.choice(numbers), random.choice(numbers), random.choice(numbers)]
        }
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

        latest_list = []
        create_list = []

        for d in list_week_day:
            create_list.append(random.choice(random_range_num))
            latest_list.append(random.choice(random_range_num))

        data = {
            'label': [i.strftime('%Y-%m-%d') for i in list_week_day],
            'latest_data': latest_list,
            'create_data': create_list,
        }

        return Response(data)
