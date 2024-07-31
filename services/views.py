from django.shortcuts import render

# Create your views here.
def services(request):
    service={'service':"active"}
    return render(request,'serv/services.html',service)
