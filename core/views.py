# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
# Create your views here.
from portfolio import settings
from .models import User
from django.conf import settings
import json
def default_response():
   return {
       settings.JSON_RESPONSE_OUTPUT_NAME: [],
       'counter':0,
       'response':{
               'status':False,
               'msg':[]
       }
   }

def user_data(request):
    username = request.GET.get('username','')
    res = default_response()
    if username:
        us = User.objects(username=username).first()
        if us:
            res['response']['username'] = us.username
            res['response']['first_name'] = us.first_name
            res['response']['last_name'] = us.last_name
            res['response']['email'] = us.email
            res['response']['status'] = True
        else:
            res['response']['msg'] = 'User Not found'
    else:

        res['response']['msg'] = 'User Not found'
    return HttpResponse(json.dumps(res))

