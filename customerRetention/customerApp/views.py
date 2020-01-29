from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.views.generic import TemplateView
from datetime import date
import datetime
import calendar

# Create your views here.


def Index(request):
    my_date = date.today()
    time = datetime.date.today()
    day = calendar.day_name[my_date.weekday()]
    context = {'time':time,'day':day}
    return render(request,'index.html', context)



# class Index(TemplateView):
#     template_name = "index.html"


    # def get_context_data(self):
    #     my_date = date.today()
    #     time = datetime.datetime.today()
    #     day = calendar.day_name[my_date.weekday()]
    #     context = {
    #         'time': time,
    #         'day': day
    #     }
    #     return context

    # def get(self, request):
    #     # <view logic>
    #     my_date = date.today()
    #     time = datetime.datetime.today()
    #     day = calendar.day_name[my_date.weekday()]
    #     context = {
    #             'time': time,
    #             'day': day
    #         }
    #     return HttpResponse(request, self.template_name,context)