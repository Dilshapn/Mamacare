from django.urls import path
from . import views
urlpatterns = [
    path('menu_page/',views.menu_page,name="menu_page"),
    path('doctor_login/',views.doctor_login,name="doctor_login"),
]