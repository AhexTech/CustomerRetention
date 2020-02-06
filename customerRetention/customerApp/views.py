from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.views.generic import TemplateView
from datetime import date
import datetime
import calendar
from django.views.generic import View
from .models import *
from django.http import JsonResponse
# Create your views here.


# def Index(request):
#     my_date = date.today()
#     time = datetime.date.today()
#     day = calendar.day_name[my_date.weekday()]
#     context = {'time':time,'day':day}
#     return render(request,'index.html', context)



class Index(View):
    def get(self, request):
        my_date = date.today()
        time = datetime.date.today()
        day = calendar.day_name[my_date.weekday()]

        data = Fruithut.objects.all()[:50]


        # print(data.get())
        Sumadd=[]
        AllUnit=[]
        for d in data:
            Sumadd.append(d.__str__()['pricesell'])
            AllUnit.append(d.__str__()['units'])



        PricesellAdded = sum(Sumadd)
        Sumunit = sum(AllUnit)
        context = {'time':time,
                   'day':day,
                   'data':data,
                   'PricesellAdded': round(PricesellAdded,2),
                   'Sumunit':Sumunit}
        return render(request, 'index.html', context)

    # def post(self, request):
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #     return render(request, 'index.html', {'form': form})


class CanvasTest(View):
    def get(self, request):
        return render(request, 'canvas.html')





class test(View):


    def get(self,request):
        data2 = Fruithut.objects.all()[:5].values()

        return JsonResponse({"Data": list(data2)})



