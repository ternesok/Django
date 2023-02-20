import random

from django.shortcuts import render
from tours import data
from random import randint


def main_view(request):

    return render(request,"index.html", context={'data': data})

def departure_view(request):
    return render(request,"departure.html")

# def tour_main_view(request):
#     return render(request,"tour.html", context={'tour': data.tours})

def tour_view(request, tour_id):

    cntx = {'tour': data.tours[tour_id]}
    return render(request,"tour.html", context=cntx)

