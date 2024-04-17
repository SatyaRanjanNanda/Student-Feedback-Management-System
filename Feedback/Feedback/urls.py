"""
URL configuration for Feedback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from Myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('studentregistration/', views.student_registration, name='studentregistration'),
    path('studentlogin/', views.student_login, name='studentlogin'),
    path('adminlogin/', views.admin_login, name='adminlogin'),
    path('adminportal/', views.admin_portal, name='adminportal'),
    path('addfaculty/', views.faculty_registration, name='addfaculty'),
    path('addstudent/', views.student_registration, name='addstudent'),
    path('feedbackform/', views.feedback_form, name='feedbackform'),
    path('viewfeedbacks/', views.view_feedbacks, name='viewfeedbacks'),
    path('totalstudents/',views.total_students,name='totalstudents'),
    path('totalfaculties/',views.total_faculties,name='totalfaculties'),
    path('delete-faculty/<int:faculty_id>/', views.delete_faculty, name='delete_faculty'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('delete-feedback/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
    path('logout_user/',views.logout_user,name="logout"),

]

