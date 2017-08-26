# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
from portfolio import settings
# Create your models here.
from mongoengine import *
connect('test')
class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    username = StringField(max_length=50)
    email = StringField()



