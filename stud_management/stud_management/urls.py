"""
URL configuration for stud_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from studapp.views import StudentView,StudentDeleteView,StudEditview
=======
from studapp.views import StudentView,StudentDeleteView
>>>>>>> 960cbdb (first commit)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',StudentView.as_view(),name='home'),
    path('delete/<int:id>',StudentDeleteView.as_view(),name='delete'),
<<<<<<< HEAD
    path('edit/<int:id>',StudEditview.as_view(),name='edit'),
=======
>>>>>>> 960cbdb (first commit)
    # path('list',StudentListview.as_view(),name='stud_list')
    
]
