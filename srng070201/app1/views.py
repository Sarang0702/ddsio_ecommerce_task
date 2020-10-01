from django.shortcuts import render

# Create your views here.
def homepage(request):
    cat = ["Electronnic Devices","Accessories","Musical Instruments"]
    return render(request,"home.html",{"cat":cat})