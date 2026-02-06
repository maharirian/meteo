from django.shortcuts import render
from django.http import HttpResponse

def show_temp_view(request):
    return HttpResponse('hamedan 27 daraje canti grad')
