import json
from urllib import response
from django.http import HttpResponse, HttpResponseBadRequest

def index(request):
    body = json.loads(request.body)

    hypotenuse = float(body["hypotenuse"])
    opposite = float(body["opposite"])
    adjacent = float(body["adjacent"])

    if not hypotenuse and opposite and adjacent:
        hypotenuse = ((opposite ** 2) + (adjacent ** 2)) ** 0.5
        return HttpResponse(hypotenuse)

    elif not opposite and hypotenuse and adjacent:
        opposite = ((hypotenuse ** 2) - (adjacent ** 2)) ** 0.5
        return HttpResponse(opposite)

    elif not adjacent and hypotenuse and opposite:
        adjacent = ((hypotenuse ** 2) - (opposite ** 2)) ** 0.5
        return HttpResponse(adjacent)

    else: 
        return HttpResponseBadRequest()
