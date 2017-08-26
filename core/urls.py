from django.conf.urls.defaults import patterns, include, url
from .views import *
urlpatterns = patterns('',
    url(r'get_user_details/$','core.views.user_data',name='user_data'),
                       )