
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def sample_view(request):    # request--- here we need request like paasing arguments from function so i taken name request instead of this we can use any name hello
    date = datetime.datetime.now()
    date1 = "<h1>Hello this is response from django app.\n Present date and time is:"+ str(date) +" </h1>"
    return HttpResponse(date1)  #----before writing this line for Httpresponce we have to
                                                                             # import django default http module of "django.http" that is 4th one line
                                                                             # and instead of "HttpResponse" name we shoudn't use any other name because this is class

