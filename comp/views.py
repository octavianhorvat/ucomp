from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

# Create your views here.


def index(request):
    licencePlates = LicencePlate.objects.all()
    for licencePlate in licencePlates:
        print(licencePlate)
    complaints = Complaint.objects.all()
    return render(request, "comp/index.html", {"licencePlates": licencePlates, "complaints": complaints})


def getPlate(request, plate):
    plate = plate.capitalize()
    return render(request, "comp/check.html", {"licencePlate": plate})


def addComplaint(request):
    if request.method == "POST":
        complaint = Complaint(description=request.POST["description"], created_at=datetime.today().strftime(
            '%Y-%m-%d'), updated_at=datetime.today().strftime('%Y-%m-%d'))
        complaint.save()
        return HttpResponseRedirect(reverse("comp:index"))
#
# try:
#     passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
#     flight = Flight.objects.get(pk=flight_id)
# except KeyError:
#     return HttpResponseBadRequest("Bad Request: no flight chosen")
# except Flight.DoesNotExist:
#     return HttpResponseBadRequest("Bad Request: flight does not exist")
# except Passenger.DoesNotExist:
#     return HttpResponseBadRequest("Bad Request: passenger does not exist")
# passenger.flights.add(flight)
# return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
