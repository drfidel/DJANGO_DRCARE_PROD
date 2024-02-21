from django.shortcuts import render

from .forms import CaptchaTestForm
from .models import Appointment,ContactUs,Department,About,Carousel,Service,SubscribeMail,Doctor,Testimony
from blog.models import Post, Comment

# Create your views here.
def indexView(request):
    about = About.objects.first()
    carousels = Carousel.objects.all()
    gservices = Service.objects.filter(department='1')
    bservices = Service.objects.filter(department='2')
    services = Service.objects.filter(realserv=1)
    departments = Department.objects.filter(realdept=1)
    doctors = Doctor.objects.all()
    testimonies = Testimony.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)

        if form.is_valid():
            try:
                subcribemail = SubscribeMail()
                subcribemail.email = request.POST.get('email')
                subcribemail.save()

                return render(request, 'drcare_FE/subscribesuccess.html', {'about' : about})
            
            except Exception:
                return render(request, 'drcare_FE/subscribefail.html')
        else:
            return render(request, 'drcare_FE/subscribefail.html')
    else:
        form = CaptchaTestForm()
    
        return render(request, 'drcare_FE/index.html', {
            'about' : about,
            'carousels' : carousels,
            'gservices' : gservices,
            'bservices': bservices,
            'services' : services,
            'departments' : departments,
            'doctors' : doctors ,
            'testimonies' : testimonies,
            'posts' : posts,
            'comments' : comments,
            'form' : form
        })

def aboutView(request):
    about = About.objects.first()
    gservices = Service.objects.filter(department='1')
    services = Service.objects.filter(realserv=1)
    departments = Department.objects.filter(realdept=1)
    testimonies = Testimony.objects.all()

    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)

        if form.is_valid():
            try:
                subcribemail = SubscribeMail()
                subcribemail.email = request.POST.get('email')
                subcribemail.save()

                return render(request, 'drcare_FE/subscribesuccess.html', {'about' : about})
            
            except Exception:
                return render(request, 'drcare_FE/subscribefail.html')
        else:
            return render(request, 'drcare_FE/subscribefail.html')
    else:
        form = CaptchaTestForm()

        return render(request, 'drcare_FE/about.html', { 
            'about' : about,
            'services' : services,
            'departments' : departments,
            'gservices' : gservices,
            'testimonies' : testimonies,
            'form': form})

def doctorView(request):
    about = About.objects.first()
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)

        if form.is_valid():
            try:
                subcribemail = SubscribeMail()
                subcribemail.email = request.POST.get('email')
                subcribemail.save()

                return render(request, 'drcare_FE/subscribesuccess.html', {'about' : about})
            
            except Exception:
                return render(request, 'drcare_FE/subscribefail.html')
        else:
            return render(request, 'drcare_FE/subscribefail.html')
    else:
        form = CaptchaTestForm()

        return render(request, 'drcare_FE/doctor.html', {
            'about' : about, 
            'doctors': doctors,
            'form': form})

def departmentView(request):
    about = About.objects.first()
    services = Service.objects.filter(realserv=1)
    departments = Department.objects.filter(realdept=1)

    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)

        if form.is_valid():
            try:
                subcribemail = SubscribeMail()
                subcribemail.email = request.POST.get('email')
                subcribemail.save()

                return render(request, 'drcare_FE/subscribesuccess.html', {'about' : about})
            
            except Exception:
                return render(request, 'drcare_FE/subscribefail.html')
        else:
            return render(request, 'drcare_FE/subscribefail.html')
    else:
        form = CaptchaTestForm()
    
        return render(request, 'drcare_FE/department.html', {
            'about' : about,
            'services' : services,
            'departments' : departments,
            'form': form })

def pricingView(request):
    about = About.objects.first()

    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)

        if form.is_valid():
            try:
                subcribemail = SubscribeMail()
                subcribemail.email = request.POST.get('email')
                subcribemail.save()

                return render(request, 'drcare_FE/subscribesuccess.html', {'about' : about})
            
            except Exception:
                return render(request, 'drcare_FE/subscribefail.html')
        else:
            return render(request, 'drcare_FE/subscribefail.html')
    else:
        form = CaptchaTestForm()
        return render(request, 'drcare_FE/pricing.html', {'about' : about, 'form': form})

def appointmentView(request):
    about = About.objects.first()
    departments = Department.objects.filter(realdept=1)
    
    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)

        appointment = Appointment()
        appointment.sirName = request.POST.get('sirName')
        appointment.firstName = request.POST.get('firstName')
        appointment.telContact = request.POST.get('telContact')
        appointment.department = request.POST.get('department')
        appointment.appointmentDate = request.POST.get('appointmentDate')
        appointment.appointmentTime = request.POST.get('appointmentTime')
        appointment.amessage = request.POST.get('amessage')
        appointment.save()

        return render(request, 'drcare_FE/success.html', {'about' : about, 'form': form})
    else:
        form = CaptchaTestForm()
        return render(request, 'drcare_FE/appointment.html', {
            'about' : about,
            'departments' : departments, 
            'form':form})

def blogView(request):
    about = About.objects.first()
    posts = Post.objects.all()
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)

        if form.is_valid():
            try:
                subcribemail = SubscribeMail()
                subcribemail.email = request.POST.get('email')
                subcribemail.save()

                return render(request, 'drcare_FE/subscribesuccess.html', {'about' : about, 'form': form})
            
            except Exception:
                return render(request, 'drcare_FE/subscribefail.html')
        else:
            return render(request, 'drcare_FE/subscribefail.html')
    else:
        form = CaptchaTestForm()

        return render(request, 'drcare_FE/blog.html', {
            'about' : about,
            'posts' : posts,
            'comments' : comments,
            'form': form
            })

def contactView(request):
    about = About.objects.first()

    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)
        
        appointment = ContactUs()
        appointment.names = request.POST.get('names')
        appointment.email = request.POST.get('email')
        appointment.subject = request.POST.get('subject')
        appointment.message = request.POST.get('message')
        appointment.save()

        return render(request, 'drcare_FE/contactsuccess.html', {'about' : about})
    else:
        form = CaptchaTestForm()
        return render(request, 'drcare_FE/contact.html', {
            'about' : about, 
            'form':form})

def blogdetailView(request):
    about = About.objects.first()

    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)

        if form.is_valid():
            try:
                subcribemail = SubscribeMail()
                subcribemail.email = request.POST.get('email')
                subcribemail.save()

                return render(request, 'drcare_FE/subscribesuccess.html', {'about' : about})
            
            except Exception:
                return render(request, 'drcare_FE/subscribefail.html', {'about' : about})
        else:
            return render(request, 'drcare_FE/subscribefail.html')
    else:
        form = CaptchaTestForm()
        return render(request, 'drcare_FE/blog-single.html', {'about' : about,'form': form})
