from django.urls import path
from pregnancyapp import views

urlpatterns = [
    path('index_page/',views.index_page,name="index_page"),
    path('filter_menu/<int:pro_id>/',views.filter_menu,name="filter_menu"),
    path('doctor_page/',views.doctor_page,name="doctor_page"),
    path('single_product/<cat_name>/',views.single_product,name="single_product"),
    path('book_page/',views.book_page,name="book_page"),
    path('book_appointment/<dr_name>/',views.book_appointment,name="book_appointment"),
    path('pregnancy_calculator/',views.pregnancy_calculator,name="pregnancy_calculator"),
    path('products/', views.product_list, name='product_list'),
    path('filter_book/<int:book_id>/',views.filter_book,name="filter_book"),
    path('appointment_save/<dr_name>/',views.appointment_save,name="appointment_save"),
    path('',views.user_login,name="user_login"),
    path('user_signup/',views.user_signup,name="user_signup"),
    path('signup_save/',views.signup_save,name="signup_save"),
    path('save_login/',views.save_login,name="save_login"),
    path('user_logout/',views.user_login,name="user_logout"),
    path('add_cart/',views.add_cart,name="add_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delete_cart/<int:cart_id>/', views.delete_cart, name="delete_cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkout_save/',views.checkout_save,name="checkout_save"),

]