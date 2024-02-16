from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('about/', views.aboutView, name='about'),
    path('doctor/', views.doctorView, name='doctor'),
    path('department/', views.departmentView, name='department'),
    path('pricing/', views.pricingView, name='pricing'),
    path('blog/', views.blogView, name='blog'),
    path('appointment/', views.appointmentView, name='appointment'),
    path('contact/', views.contactView, name='contact'),
    path('blogdetail/', views.blogdetailView, name='blogdetail'),
]