from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from sites import models,views
from django.views.generic import UpdateView,TemplateView,ListView,DetailView

import json
from django.core import serializers
from django.db.models import Sum
from django.db.models.aggregates import Avg,Sum,Count

from sites.models import sites

def home(request):
    model = sites
    sites_list = sites.objects.all()
    context = {
        'object_list': sites_list
    }
    return render(request, "sites/sites_list.html", context)

def summary_infomation(request):
    model = sites
    total = sites.objects.values('site_name').annotate(sumAvalue = Sum('Avalue')).annotate(sumBvalue = Sum('Bvalue'))
    context = {
        'object_list': total
    }
    return render(request, "sites/summary.html", context)

def summary_average(request):
    model = sites
    Average = sites.objects.values('site_name').annotate(avgAvalue = Avg('Avalue')).annotate(avgBvalue = Avg('Bvalue'))

    context = {
        'object_list': Average
    }
    return render(request, "sites/summary_average.html", context)
