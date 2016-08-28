from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.views.generic import UpdateView,TemplateView,ListView,DetailView
from .models import sites
import json
from django.core import serializers

class SitesList(ListView):

        def get_queryset(self):
            queryset = sites.objects.all()
            return queryset

def sites_detail(request,pk):
    model = sites
    result = sites.objects.filter(id=pk).values('site_name')
    query = sites.objects.filter(site_name=result).values('Avalue','Bvalue','Date','site_name')
    context={
        'object_list': query
    }
    return render(request, "sites/sites_information.html", context)