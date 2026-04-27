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

    def get(self, request, id):
        student = StudentModel.objects.get(id=id)
        student.delete()
        return redirect('home')
    
    
# class StudEditview(View):
    
#     def get(self,request,*args, **kwargs):
        
#         stud=StudentModel.objects.get(id=id)    