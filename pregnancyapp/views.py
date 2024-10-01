from django.shortcuts import render,redirect
from adminapp.models import Category_db,book_db,Doctor_db,product_db
from pregnancyapp.models import patient_db,register_db,cart_db,proceed_db
from decimal import Decimal, InvalidOperation
from django.contrib import messages


# Create your views here.
def index_page(request):
    data = Category_db.objects.all()
    books = product_db.objects.filter(category='Baby & Bump Books')
    return render(request,"index.html",{'data':data,'books':books})
def filter_menu(request,pro_id):
    pro = product_db.objects.get(id=pro_id)
    return render(request,"filter_menu.html",{'pro':pro})
def doctor_page(request):
    doc = Doctor_db.objects.all()
    return render(request,"doctor.html",{'doc':doc})
def single_product(request,cat_name):
    cat = product_db.objects.filter(category=cat_name)
    pro = Category_db.objects.all()
    return render(request,"single_product.html",{'cat':cat,'pro':pro})
def book_page(request):
    book = book_db.objects.all()
    return render(request,"book_page.html",{'book':book})
def book_appointment(request,dr_name):
    doc = Doctor_db.objects.get(Name=dr_name)
    return render(request,"book_appointment.html",{'doc':doc,'dr_name': dr_name})
def appointment_save(request,dr_name):
    if request.method=="POST":
        a = request.POST.get('doctor')
        b = request.POST.get('patient')
        c = request.POST.get('phone')
        d = request.POST.get('date')
        e = request.POST.get('time')
        obj = patient_db(doctor_name=a,patient_name=b,contact=c,date=d,time=e)
        obj.save()
        return redirect(book_appointment,dr_name=dr_name)
def pregnancy_calculator(request):
    return render(request, 'preg_calculator.html')

def product_list(request):
    products = product_db.objects.all()
    error_message = None

    # Get price filter values from the request
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Convert to Decimal and filter products
    if min_price:
        try:
            min_price = Decimal(min_price)
            products = products.objects.filter(price__gte=min_price)
        except InvalidOperation:
            error_message = "Invalid value for minimum price. Please enter a valid number."

    if max_price:
        try:
            max_price = Decimal(max_price)
            products = product_db.objects.filter(price__lte=max_price)
        except InvalidOperation:
            error_message = "Invalid value for maximum price. Please enter a valid number."

    # Pass the products and error message to the template
    return render(request, 'single_product.html', {'products': products, 'error_message': error_message})

def filter_book(request,book_id):
    book = book_db.objects.get(id=book_id)
    return render(request,"filter_book.html",{'book':book})
def user_login(request):
    return render(request,"user_login.html")
def user_signup(request):
    return render(request,"user_signup.html")
def signup_save(request):
    if request.method=="POST":
        un = request.POST.get('username')
        em = request.POST.get('email')
        ps = request.POST.get('password')
        obj = register_db(username=un,email=em,password=ps)
        obj.save()
        return redirect(user_login)
def save_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        ps = request.POST.get('password')
        if register_db.objects.filter(username=un,password=ps).exists():
            request.session['username'] = un
            request.session['password'] = ps
            messages.success(request, "Welcome User")
            return redirect(index_page)
        else:
            messages.error(request, "User not found")
            return redirect(user_login)
    else:
        messages.error(request, "Incorrect Password")
        return redirect(user_login)
def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(index_page)
def add_cart(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        qt = request.POST.get('quantity')
        pr = request.POST.get('price')
        nm = request.POST.get('pro_name')
        tp = request.POST.get('total_price')
        obj = cart_db(User_Name=un,Quantity=qt,Price=pr,Product_Name=nm,Total_Price=tp)
        obj.save()
        return redirect(index_page)
def cart_page(request):
    data = Category_db.objects.all()
    cat = cart_db.objects.filter(User_Name=request.session['username'])
    subtotal = 0
    shipping = 0
    total = 0
    for i in cat:
        subtotal+=i.Total_Price
        if subtotal>3000:
            shipping = 150
        else:
            shipping = 250
        total = subtotal+shipping
    return render(request,"cart_page.html",{'cat':cat,'subtotal':subtotal, 'shipping':shipping,'total':total,'data':data})

def delete_cart(request,cart_id):
    x = cart_db.objects.filter(id=cart_id)
    x.delete()
    return redirect(cart_page)
def checkout(request):
    cat = cart_db.objects.filter(User_Name=request.session['username'])
    subtotal = 0
    shipping = 0
    total = 0
    for i in cat:
        subtotal += i.Total_Price
        if subtotal > 3000:
            shipping = 150
        else:
            shipping = 250
        total = subtotal + shipping
    return render(request,"checkout.html",{'cat':cat,'subtotal':subtotal,'shipping':shipping,'total':total})
def checkout_save(request):
    if request.method == "POST":
        b = request.POST.get('name')
        c = request.POST.get('country')
        d = request.POST.get('address')
        e = request.POST.get('town')
        f = request.POST.get('state')
        g = request.POST.get('pin')
        h = request.POST.get('phone')
        i = request.POST.get('email')
        j = request.POST.get('price')
        obj = proceed_db(Name=b,Country=c,Address=d,Town=e,State=f,Pincode=g,Phone=h,Email=i,total_price=j)
        obj.save()
        return redirect(index_page)
def wishlist_page(request):
    if request.method=="POST":
        us = request.POST.get('')
        pd = request.POST.get('')
        img = request.POST.get('')
        pr = request.POST.get('')




