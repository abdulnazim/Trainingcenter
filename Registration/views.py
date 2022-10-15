from django.shortcuts import render
from django.http import HttpResponse
from Registration.models import Course,Batch,Student


# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Prime Intuit Registration page</h1>")
def Home(request):
    # return HttpResponse("<h1>Welcome to Prime Intuit Home</h1>")
    # my_dict={'Insert_Me':"I am a text from Registration/Views.py now from sub template"}
    # batch_list=Batch.objects.order_by('batch_ID')
    batch_list = Batch.objects.raw('select * from Registration_batch where start_date>"2021-06-01"')
    data_dict={'access_record':batch_list,'Insert_Me':"I am a text from Registrations"}

    return render(request,'Registration/index.html',context=data_dict)