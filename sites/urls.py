from django.conf.urls import url
from . import views
from sites.views import *

#urlpatterns = [
# ex: /sites/
#url(r'^$', SitesList.as_view(), name='siteslist'),
#url(r'^(?P<pk>\d+)$', SitesDetail.as_view(), name='sitesdetail'),
        #]

urlpatterns = [
    url(r'^$',SitesList.as_view()),
    url(r'^(?P<pk>\d+)',sites_detail),
    ]