# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def News_view(request):
    return render(request, "NewsAppTMPTS/results.html")
def Politics_view(request):
    line1 = "in April month election is there in AP."
    line2 = "Uproar in T.N. Congress over choice of Karti"
    line3 = "MDMK agrees to contest on DMK symbol in Erode"
    line4 = "Modi meetings in State on March 29, April 1"
    line5 = "Will not allow Jagan to run Pulivendula politics in State"
    dict = {"line1":line1, "line2":line2, "line3":line3,"line4":line4, "line5":line5}
    return render(request, "NewsAppTMPTS/Politics.html", dict)

def Sports_view(request):
    head1 = "It will be a battle where experience will be pitted against youth"
    head2 = "Harbhajan, after his man of the match performance against RCB"
    head3 = "Chennai Super Kings: MS Dhoni (captain & WK), Suresh Raina"
    head4 = "Billings, Ravindra Jadeja, Dhruv Shorey, Chaitanya Bishnoi"
    dict1 = {"head1":head1, "head2":head2, "head3":head3, "head4":head4}
    return render(request, "NewsAppTMPTS/Sports.html", dict1)

def Technology_view(request):
    main1 = "Modi meetings in State on March 29, April 1"
    main2 = "Will not allow Jagan to run Pulivendula politics in State"
    main3 = "MDMK agrees to contest on DMK symbol in Erode"
    main4 = "in April month election is there in AP."
    dict2 = {"main1":main1, "main2":main2, "main3":main3, "main4":main4}
    return render(request, "NewsAppTMPTS/Technology.html", dict2)

