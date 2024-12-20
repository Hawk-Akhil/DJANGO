from django.shortcuts import render
import csv
def items(request):
    return render(request,"item.html")
def nike(request):
    return render(request,"nike.html")
def glasses(request):
    return render(request,"glasses.html")
def denim(request):
    return render(request,"denim.html")
def fastrack(request):
    return render(request,"fastrack.html")
def iphone(request):
    return render(request,"iphone.html")
def trouser(request):
    return render(request,"trouser.html")
def poco(request):
    return render(request,"poco.html")
def kvs(request):
    return render(request,"kvs.html")
def screw(request):
    return render(request,"screw.html")
def formal(request):
    return render(request,"formal.html")
def denver(request):
    return render(request,"denver.html")
def submit(request):
    if request.method=='POST':
        dict1=request.POST
        with open('data.csv','a') as csvfile:
            wrt=csv.writer(csvfile)
            for key,value in dict1.items():
                wrt.writerow([key,value])
    return render(request,'submit.html')            
def login(request):
    if request.method=='POST':
        dict2=request.POST
        with open('order.csv','a')as csvfilee:
            wtr=csv.writer(csvfilee)
            for key,value in dict2.items():
                wtr.writerow([key,value])
    return render(request,'login.html')






