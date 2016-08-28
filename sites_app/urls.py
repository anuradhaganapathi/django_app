"""sites_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from sites_app.views import summary_infomation,home,summary_average
from django.views.generic import UpdateView,TemplateView,ListView,DetailView

urlpatterns = [
   # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view= home ),
    url(r'^sites/', include('sites.urls')),
    url(r'^summary/', view = summary_infomation),
    url(r'^summary-average/', view = summary_average),

]
