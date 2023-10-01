from django.shortcuts import render
from myapp.models import Employee
from myapp.forms import MyForm

def my_forms(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
    else:
        form = MyForm()
    return render(request,"index.html",{"form":form})