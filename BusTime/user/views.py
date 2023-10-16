from django.shortcuts import render
# from django.http import HttpResponse
from driver.models import Bustime
from .forms import BusScheduleSearch

# Create your views here.
def table(request):
    obj=Bustime.objects.all()
    return render(request,'user/table.html',{'data':obj})

def bus_search(request):
    if request.method=='POST':
        form=BusScheduleSearch(request.POST)
        if form.is_valid():
            b_from=form.cleaned_data['b_from']
            to=form.cleaned_data['to']
            results=Bustime.objects.filter(to__icontains=to,b_from__icontains=b_from)
            return render(request,'user/search_page.html',{'bus_schedules':results,'msg':'No result'})
        else:
            bus_schedules=[]
            # return HttpResponse("No Result")
            # return render(request,'user/search_page.html',{'form':form,'bus_schedules':bus_schedules})
    else:
        form=BusScheduleSearch()
        bus_schedules=[]
    return render(request,'user/search_page.html',{'form':form,'bus_schedules':bus_schedules})

def index1(request):
    return render(request,'user/u_index.html')


