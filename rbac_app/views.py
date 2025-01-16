from django.http import HttpResponse

# Home view function
def home(request):
    return HttpResponse("Welcome to the RBAC System!")
