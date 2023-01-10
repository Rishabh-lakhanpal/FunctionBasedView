from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import StudentRegistration
# Create your views here.

# This Function will Add new Item and Show all items
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
        form = StudentRegistration()
    else:
        form = StudentRegistration()
    # stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':form, 'stud':User.objects.all()})

# This Function will Delete

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#This Function will updateor edir

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form= StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form= StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':form})