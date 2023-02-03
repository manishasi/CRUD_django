from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from.models import user

# Create your views here.
# This Function Will Add new Item and Show All Items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # print(fm)
            # fm.save()
            nm=fm.cleaned_data['name']
            # print(nm)
            em=fm.cleaned_data['email']
            # print(em)
            pw=fm.cleaned_data['password']
            # print(pw)
            reg = user(name=nm, email=em, password=pw)
            reg.save()
            # print(reg)
            # print(fm)
            fm = StudentRegistration()
            return HttpResponseRedirect('/')
            

    else:
        fm = StudentRegistration()
    stud = user.objects.all()
    # for i in stud:
        # print(i.name)
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#This Function Will Update/Edit
def update_data(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        print(pi)
        fm = StudentRegistration(request.POST,instance=pi )
        print(request.POST)
        # print(fm,"result")
        if fm.is_valid():
            fm.save()
        print(fm)
        return HttpResponseRedirect('/')
    else:
        pi = user.objects.get(pk=id)
        print(pi)
        fm = StudentRegistration(instance=pi)
        print(fm)
    return render(request,'enroll/update.html',{'form':fm})

# This Function Will Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
