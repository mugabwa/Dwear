from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import redirect, render
from routes.models import Route, RouteData
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core import serializers


from routes.forms import FileForm

@csrf_exempt
def loadData(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        info = dict(item.split("=") for item in data.split("#"))
        origin = info.get('origin')
        destination = info.get('destination')
        cost = "{:.2f}".format(float(info.get('cost')))
        distance = info.get('distance')
        if origin and destination and cost and distance:
            obj = Route.objects.create(origin=origin, destination=destination,
            distance=distance,cost=cost)
            obj.save()
        return HttpResponse(obj.id)
    return HttpResponse("Data not loaded")

@csrf_exempt
def fetchData(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        info = dict(item.split("=") for item in data.split("#"))
        origini = info.get('origin')
        destinationi = info.get('destination')
        if origini and destinationi:
            if Route.objects.filter(origin=origini,destination=destinationi):
                obj = Route.objects.values_list('cost').get(origin=origini, destination=destinationi)
                print(obj)
                return HttpResponse(obj[0])
            else:
                print("Not present")
                return HttpResponse("ERROR:-Not found")

    return HttpResponse("ERROR:-Not found")

@csrf_exempt
def stopData(request):
    if request.method=='POST':
        data = request.POST.get('data')
        id = data.split('=')[1]

        print(id)
    return HttpResponse("SUCCESS")
@csrf_exempt
def sendData(request):
    if request.method=="POST":
        data = request.POST.get('data')
        print(data)
    return HttpResponse("SUCCESS")

@csrf_exempt
def uploadFile(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('route-list')
    else:
        form = FileForm()
    return render(request, 'mfile.html', {'form': form})