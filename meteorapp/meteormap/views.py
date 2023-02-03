from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Index page")


def map_view(request):
    return HttpResponse("The map page")
