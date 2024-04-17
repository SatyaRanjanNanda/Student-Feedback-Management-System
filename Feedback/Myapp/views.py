from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def feedback_form(request):
    if request.method == 'POST':
        teacher = request.POST.get('teacher')
        subject = request.POST.get('subject')
        clarity = request.POST.get('clarity')
        engagement = request.POST.get('engagement')
        approachability = request.POST.get('approachability')
        management = request.POST.get('management')
        fairness = request.POST.get('fairness')
        encouragement = request.POST.get('encouragement')
        organization = request.POST.get('organization')
        teaching = request.POST.get('teaching')
        satisfaction = request.POST.get('satisfaction')
        message = request.POST.get('message')

        feedback_instance = Feedback.objects.create(
            teacher=teacher,
            subject=subject,
            clarity=clarity,
            engagement=engagement,
            approachability=approachability,
            management=management,
            fairness=fairness,
            encouragement=encouragement,
            organization=organization,
            teaching=teaching,
            satisfaction=satisfaction,
            message=message
        )
        feedback_instance.save()
        admin_dashboard = Admin_Dashboard.objects.first()
        admin_dashboard.total_feedback += 1
        admin_dashboard.save()

        return HttpResponse('Feedback submitted successfully')
    faculties = Faculty.objects.all()
    return render(request, 'feedbackform.html', {'faculties': faculties})

def student_registration(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not (full_name and email and password and confirm_password):
            return redirect('studentregistration')

        if password != confirm_password:
            return render(request, 'studentregistration.html', {'error': 'Passwords do not match'})

        if Student.objects.filter(email=email).exists():
            return render(request, 'studentregistration.html', {'error': 'Email already exists'})

        student = Student.objects.create(full_name=full_name, email=email)

        admin_dashboard = Admin_Dashboard.objects.first()
        admin_dashboard.total_students += 1
        admin_dashboard.save()

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        return redirect('studentlogin')

    else:
        return render(request, 'studentregistration.html')

def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)


        user = authenticate(request, username=email, password=password)

        if user is not None:

            login(request, user)
            return redirect('feedbackform')
        else:

            return render(request, 'studentlogin.html', {'error': 'Invalid email or password'})

    else:
        return render(request, 'studentlogin.html')


def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        user = authenticate(request, username=email, password=password)

        if user is not None:

            login(request, user)

            return redirect('adminportal')
        else:
            return redirect('adminlogin')
    else:
        return render(request, 'adminlogin.html')


def admin_portal(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')

    admin_dashboard = get_object_or_404(Admin_Dashboard)
    return render(request, 'adminportal.html', {'admin_dashboard': admin_dashboard})

def view_feedbacks(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'totalfeedbacks.html', {'feedbacks': feedbacks})


def faculty_registration(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        subject = request.POST.get('subject')

        faculty = Faculty.objects.create(full_name=full_name, subject=subject)
        faculty.save()


        admin_dashboard = Admin_Dashboard.objects.first()
        admin_dashboard.total_faculties += 1
        admin_dashboard.save()

        return HttpResponse('Faculty registered successfully')

    else:
        return render(request, 'addfaculty.html')

def total_students(request):
    students = Student.objects.all()
    return render(request, 'totalstudents.html', {'students': students})

def total_faculties(request):
    faculties = Faculty.objects.all()
    return render(request, 'totalfaculties.html', {'faculties': faculties})

def delete_faculty(request, faculty_id):
    if request.method == 'POST':
        try:
            faculty = Faculty.objects.get(pk=faculty_id)
            faculty.delete()
            return redirect('totalfaculties')
        except Faculty.DoesNotExist:
            return HttpResponse('Faculty not found')
    else:
        return HttpResponse('Invalid request method')

def delete_student(request, student_id):
    if request.method == 'POST':
        try:
            student = Student.objects.get(pk=student_id)
            student.delete()
            return redirect('totalstudents')
        except Student.DoesNotExist:
            return HttpResponse('Student not found')
    else:
        return HttpResponse('Invalid request method')


def delete_feedback(request, feedback_id):
    if request.method == 'POST':
        try:
            feedback = Feedback.objects.get(pk=feedback_id)
            feedback.delete()
            return redirect('viewfeedbacks')
        except Feedback.DoesNotExist:
            return HttpResponse('Feedback not found')
    else:
        return HttpResponse('Invalid request method')

def logout_user(request):
    logout(request)
    return redirect('adminlogin')