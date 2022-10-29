from fileinput import filename
from django.shortcuts import render
from .forms import FileForm
from .models import Vehicle
import json
from .utils import *

# Create your views here.


def index(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = json.load(request.FILES["file"])
            for row in file:
                if validateData(row):
                    checkCar = getCar(row["model_year"], row["make"], row["model"])
                    if checkCar:
                        updateData(checkCar, row)
                    else:
                        newData = Vehicle(
                            model_year=row["model_year"],
                            make=row["make"],
                            model=row["model"],
                            rejection_percentage=row["rejection_percentage"],
                            reason_1=row["reason_1"],
                            reason_2=row["reason_2"],
                            reason_3=row["reason_3"],
                        )
                        newData.save()
    else:
        form = FileForm()
    #encoding json file that could work with
    json_data = json.dumps(list(Vehicle.objects.values()))

    return render(request, "index.html", {"form": form, "json_data": json_data})
