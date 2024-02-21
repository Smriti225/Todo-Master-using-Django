from django.shortcuts import render,HttpResponse,redirect
from .models import task_data

def todo_Master(request):
    if request.method=="GET":
     return render(request,"taskmaster.html",{"tasks":task_data.objects.all()})
    if request.method=="POST":
        data=request.POST.get("title")
        task=task_data.objects.create(title=data)
        return render(request,"taskmaster.html",{"tasks":task_data.objects.all()})
def edit_task(request,id):
    if request.method=="GET":
        if id:
            data=task_data.objects.get(id=id)
            return render(request,"edit_task.html",{"task":data})
    elif request.method=="POST":
        data = request.POST.get("title")
        if id:
            task = task_data.objects.get(id=id)
            task.title = data
            task.save()
            return redirect("/todo")

    

def delete_task(request,id):
    if id:
       data=task_data.objects.get(id=id)
       data.delete()
       return redirect("/todo")
    else:
       return HttpResponse({"message":"Id does not exits"})