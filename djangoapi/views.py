from django.http import HttpResponse

def index(request):
    hypotenuse = 5
    opposite = ""
    adjacent = 3

    if hypotenuse == "":
        hypotenuse = (opposite * opposite + adjacent * adjacent) ** (1 / 2)
        return HttpResponse(hypotenuse)

    elif opposite == "":
        opposite = (hypotenuse * hypotenuse - adjacent * adjacent) ** (1 / 2)
        return HttpResponse(opposite)

    elif adjacent == "":
        adjacent = (hypotenuse * hypotenuse - opposite * opposite) ** (1 / 2)
        return HttpResponse(adjacent)