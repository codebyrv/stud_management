from django.shortcuts import render, redirect
from django.views import View
from studapp.models import StudentModel


class StudentView(View):

    def get(self, request):
        data = StudentModel.objects.all()
        return render(request, 'home.html', {"data": data})

    def post(self, request):
        n = request.POST.get("name")
        a = request.POST.get("age")
        e = request.POST.get("email")
        p = request.POST.get("phone")

        StudentModel.objects.create(
            stud_name=n,
            age=a,
            email=e,
            phone=p
        )

        return redirect('home')


class StudentDeleteView(View):

<<<<<<< HEAD
    def get(self, request,*args, **kwargs):
        studid=kwargs.get('id')
        student = StudentModel.objects.get(id=studid)
=======
    def get(self, request, id):
        student = StudentModel.objects.get(id=id)
>>>>>>> 960cbdb (first commit)
        student.delete()
        return redirect('home')
    
    
<<<<<<< HEAD
class StudEditview(View):
    
    def get(self,request,*args, **kwargs):
        
        studid=kwargs.get('id')
        
        
        stud=StudentModel.objects.get(id=studid)   
        
        return render (request,'stud_edit.html',{"data":stud})
    
    
    def post(self,request,*args, **kwargs):
        
        id=kwargs.get('id')
        
        
        student=StudentModel.objects.get(id=id)
        student.stud_name=request.POST.get("name")
        student.age=request.POST.get("age")
        student.email=request.POST.get("email")
        student.phone=request.POST.get("phone")
        
        student.save()
        return redirect('home')
    
        
        
         
=======
# class StudEditview(View):
    
#     def get(self,request,*args, **kwargs):
        
#         stud=StudentModel.objects.get(id=id)    
>>>>>>> 960cbdb (first commit)
