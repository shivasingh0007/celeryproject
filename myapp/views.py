from django.shortcuts import render
from myceleryproject.celery import add
from myapp.task import sub
from celery.result import AsyncResult
# Create your views here.
# def index(request):
#     print("Request: ")
#     result1=sub.delay(100,20)
#     print("Result 1: ",result1)
#     result2=add.delay(100,20)
#     print("Result 1: ",result2)
#     return render(request,"myapp/home.html")


# Enqueue Task using apply_async()
# def index(request):
#     print("Request: ")
#     result1=sub.apply_async(args=[100,20])
#     print("Result 1: ",result1)
#     result2=add.apply_async(args=[100,20])
#     print("Result 1: ",result2)
#     return render(request,"myapp/home.html")

def index(request):
    result1=sub.delay(100,20)
    return render(request,"myapp/home.html",{"result1":result1})

def check_result(request,task_id):
    result=AsyncResult(task_id)
    print("Ready: ",result.ready())
    print("Successfull: ",result.successful())
    print("Faild: ",result.failed())
    return render(request,"myapp/result.html",{'result':result})

def about(request):
    print("Request: ")
    return render(request,"myapp/about.html")
def contact(request):
    print("Request: ")
    return render(request,"myapp/contact.html")