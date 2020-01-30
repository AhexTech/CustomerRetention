from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.views.generic import TemplateView
from datetime import date
import datetime
import calendar
from django.views.generic import View
from .models import *

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
        context = {'time':time,'day':day}
        return render(request, 'index.html', context)

    # def post(self, request):
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #     return render(request, 'index.html', {'form': form})


