from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from client.models import CustomUser
from routes.models import Route
from routes.process_data import cost_data


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


def addFileToDB(file_path, pk):
    route = Route.objects.get(id = pk)
    route.filepath = file_path
    cost = cost_data(str(file_path))
    print(cost)
    route.calculated_cost = cost
    route.cost_status = True
    route.save()

@csrf_exempt
def sendData(request):
    if request.method=="POST":
        if request.FILES:
            file_id = request.POST.get('file_id')
            file = request.FILES.get('data')
            path = default_storage.save(file.name,ContentFile(file.read()))
            addFileToDB(path, file_id)
            # print(path, file_id)
            return HttpResponse("RECEIVED")
    return HttpResponseBadRequest("ERROR OCCURRED!!!")


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        info = dict(item.split("=") for item in data.split("#"))
        email = info.get('email')
        psw = info.get('pwd')
        reg = CustomUser.objects.create_user(email=email,password=psw)
        try:
            reg.save()
            return HttpResponse(reg)
        except IntegrityError:
            return HttpResponse("Key already exists")
    return HttpResponse("Error in communication!")

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        info = dict(item.split("=") for item in data.split("#"))
        email = info.get('email')
        psw = info.get('pwd')
        user = authenticate(username=email, password = psw)
        print(user)
        print(info)
        if user is not None:
            return HttpResponse(user.id)
        else:
            return HttpResponse("Failed to login")
    return HttpResponse("Error in communication")