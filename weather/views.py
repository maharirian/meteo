from django.shortcuts import render
import random

def show_temp_view(request):
    temp = random.randint(1,30)
    context = {"city":"hamedan","temp":temp}
    return render(request ,"show_temp.html",context)
