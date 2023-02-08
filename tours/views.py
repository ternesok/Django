from django.shortcuts import render
from tours import data



def main_view(request):
    return render(request,"index.html", context={'data': data})

def departure_view(request):
    return render(request,"departure.html")

def tour_view(request, tour_id):
    return render(request,"tour.html", context={'tour': data.tours[tour_id]})
