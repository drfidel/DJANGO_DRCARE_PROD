from django.contrib import admin

# Register your models here.
from .models import Appointment, ContactUs, Department, About, Service, ContactUs, Carousel, Doctor, SubscribeMail,Testimony

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ['id','sirName', 'firstName', 'telContact', 'department','appointmentDate','appointmentTime', 'amessage']
	list_filter = ['appointmentDate', 'department']
	search_fields = ['sirName','firstName','telContact']
	date_hierarchy = 'appointmentDate'
	ordering = ['appointmentDate', 'appointmentTime']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
	list_display = ['subject', 'names', 'mailingDate', 'email']
	list_filter = ['mailingDate']
	search_fields = ['names','subject']
	date_hierarchy = 'mailingDate'
	ordering = ['mailingDate']

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
	list_display = ['author', 'occupation']
	search_fields = ['author']
admin.site.register(Department)
admin.site.register(About)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['serviceTitle', 'department']
	list_filter = ['department','realserv']
	search_fields = ['serviceTitle']

@admin.register(SubscribeMail)
class SubscribeAdmin(admin.ModelAdmin):
	list_display = ['email']

admin.site.register(Carousel)
admin.site.register(Doctor)
