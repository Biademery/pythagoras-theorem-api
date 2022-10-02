from django.http import HttpResponse

def index(request):
    result = "This would be my result"
    return HttpResponse(result)