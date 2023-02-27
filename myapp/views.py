from django.shortcuts import render,HttpResponse,get_object_or_404
from  .models import employee


def index(request):
    res=employee.objects.all().order_by('id')
    data={"result":res}
    return render(request,'index.html',data)


def detail(request,id):
    mydata=get_object_or_404(employee,id=id)
    res={"post":mydata}
    return render(request,'detail.html',res)
# Create your views here.

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        designation=request.POST.get('designation')
        salary=request.POST.get('salary')
        mobile_no=request.POST.get('mobile_no')
        data=employee(name=name,designation=designation,salary=salary,mobile_no=mobile_no)
        data.save()
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')