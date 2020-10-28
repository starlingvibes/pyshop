from django.http import HttpResponse
from django.shortcuts import render
from .models import Offer


def index(request):
    offers = Offer.objects.all()
    return render(request, "./index2.html/", {"offers": offers})
