from django.shortcuts import render
def fun(request):
    return render (request,'map.html')
def city(request):
    return render (request,'city.html')
def college(request):
    return render (request,'college.html')
def ground(request):
    return render (request,'ground.html')
def park(request):
    return render (request,'park.html')
def temple(request):
    return render (request,'temple.html')
def map(request):
    return render (request,'map')

# Create your views here.
