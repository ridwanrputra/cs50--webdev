from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# task = ["foo","bar","baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label = "Priority",min_value=1,max_value = 8)

def index(request):
    if "task" not in request.session:
        request.session["task"]=[]

    return render(request,"task/index.html",{
        "task":request.session["task"]
    })

def add(request):
    if request.method == "POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task_temp = form.cleaned_data["task"]
            request.session["task"] += [task_temp]
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"task/add.html",{
                "form":form
            })

    return render(request,"task/add.html",{
        "form": NewTaskForm()
    })
