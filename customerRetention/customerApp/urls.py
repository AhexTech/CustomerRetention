"""customerRetention URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from django.conf.urls import include, url
from customerApp.views import Index
from customerApp import views

urlpatterns = [
    # url(r'^$', Index, name="index"),
    # url(r'^contact/$', contact, name='contact'),
    url(r'^$', views.Index.as_view(), name='Index'),
    url(r'^canvas/$', views.CanvasTest.as_view(), name='Canvas'),
    url(r'^test/$', views.test.as_view(), name='test'),
    url(r'^testJson/$', views.testJson.as_view(), name='testJson'),
    # url(r'^tesstForm/$', views.tesstForm.as_view(), name='tesstForm'),

]



# from customerApp.views import Index
#
# urlpatterns = [
#     url(r'^$', Index.as_view()),
# ]


