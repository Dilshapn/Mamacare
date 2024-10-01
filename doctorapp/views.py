from django.shortcuts import render
from pregnancyapp.models import patient_db
from django.contrib.auth.decorators import login_required
def menu_page(request):
    return render(request,"menu.html")
def doctor_login(request):
    return render(request,"doctor_login.html")
