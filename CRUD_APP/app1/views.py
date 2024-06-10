from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = StudentForm()
    students = Student.objects.all().order_by('roll')
    return render(request,'app1/home.html',{'form':form,'students':students})

def StudentDelete(request,roll):
    if request.method == 'POST':
        student = Student.objects.get(pk=roll)
        student.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
def StudentUpdate(request,roll):
    student = Student.objects.get(pk=roll)
    form = StudentForm(request.POST,instance=student)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = StudentForm(instance=student)
    return render(request,'app1/update.html',{'form':form})
        
    