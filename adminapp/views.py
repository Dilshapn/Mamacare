from django.shortcuts import render,redirect
from adminapp.models import Doctor_db,Category_db,book_db,product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def home_page(request):
    return render(request,"home.html")
def add_doctor(request):
    return render(request,"add_doctors.html")
def save_doctor(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('qualification')
        c = request.POST.get('email')
        d = request.POST.get('interest')
        e = request.POST.get('phone')
        f = request.POST.get('hospital')
        g = request.POST.get('place')
        h = request.POST.get('district')
        image = request.FILES['image']
        obj = Doctor_db(Name=a,Qualification=b,Email=c,Interest=d,Phone=e,Hospital=f,Place=g,District=h,Image=image)
        obj.save()
        messages.success(request, "Doctor profile created successfully!")
        return redirect(add_doctor)
def display_doctor(request):
    data = Doctor_db.objects.all()
    return render(request,"doctor_display.html",{'data':data})
def edit_doctor(request,doc_id):
    data = Doctor_db.objects.get(id=doc_id)
    return render(request,"edit_doctor.html",{'data':data})
def edit_save(request,doc_id):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('qualification')
        c = request.POST.get('email')
        d = request.POST.get('interest')
        e = request.POST.get('phone')
        f = request.POST.get('hospital')
        g = request.POST.get('place')
        h = request.POST.get('district')
        try:
            Image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Image.name,Image)
        except MultiValueDictKeyError:
            file = Doctor_db.objects.get(id=doc_id).Image
        Doctor_db.objects.filter(id=doc_id).update(Name=a,Qualification=b,Email=c,Interest=d,Phone=e,Hospital=f,Place=g,District=h,Image=file)
        messages.success(request, "Doctor profile Edited successfully!")
        return redirect(display_doctor)
def delete_doctor(request,doc_id):
    x = Doctor_db.objects.filter(id=doc_id)
    x.delete()
    messages.error(request,"Doctor profile deleted")
    return redirect(display_doctor)
def add_food(request):
    return render(request,"add_food.html")
def add_save(request):
    if request.method=="POST":
        a = request.POST.get('category')
        b = request.POST.get('description')
        image = request.FILES['image']
        obj = Category_db(category=a,description=b,image=image)
        obj.save()
        messages.success(request, "Doctor profile Edited successfully!")
        return redirect(add_food)
def display_cat(request):
    product = Category_db.objects.all()
    return render(request,"display_cat.html",{'product':product})
def edit_cat(request,edit_id):
    product = Category_db.objects.get(id=edit_id)
    return render(request,"edit_cat.html",{'product':product})
def cat_save(request,edit_id):
    if request.method=="POST":
        a = request.POST.get('category')
        b = request.POST.get('description')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name,image)
        except MultiValueDictKeyError:
            file = Category_db.objects.get(id=edit_id).image
        Category_db.objects.filter(id=edit_id).update(category=a,description=b,image=file)
        return redirect(display_cat)
def delete_category(request,del_id):
    x = Category_db.objects.get(id=del_id)
    x.delete()
    return redirect(display_cat)

def add_books(request):
    return render(request,"add_books.html")
def save_book(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('author')
        c = request.POST.get('price')
        d = request.FILES['image']
        obj = book_db(book_name=a,author=b,price=c,image=d)
        obj.save()
        return redirect(add_books)
def display_book(request):
    book = book_db.objects.all()
    return render(request,"display_book.html",{'book':book})
def edit_book(request,book_id):
    data = book_db.objects.get(id=book_id)
    return render(request,"edit_book.html",{'data':data})
def book_edit(request,book_id):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('author')
        c = request.POST.get('price')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name,image)
        except MultiValueDictKeyError:
            file = book_db.objects.get(id=book_id).image
        book_db.objects.filter(id=book_id).update(book_name=a,author=b,price=c,image=file)
        return redirect(display_book)
def del_book(request,book_id):
    x = book_db.objects.get(id=book_id)
    x.delete()
    return redirect(display_book)

def category_page(request):
    cat = Category_db.objects.all()
    return render(request,"category_page.html",{'cat':cat})

def save_category(request):
    if request.method=="POST":
        a = request.POST.get('category')
        b = request.POST.get('name')
        d = request.POST.get('price')
        pro_image1 = request.FILES['image1']
        pro_image2 = request.FILES['image2']
        pro_image3 = request.FILES['image3']
        obj = product_db(category=a,item=b,price=d,image1=pro_image1,image2=pro_image2,image3=pro_image3)
        obj.save()
        messages.success(request, "Category added successfully!")
        return redirect(category_page)

def display_category(request):
    product = product_db.objects.all()
    return render(request,"display_category.html",{'product':product})

def edit_category(request,edit_id):
    pro = Category_db.objects.all()
    cat = product_db.objects.get(id=edit_id)
    return render(request,"edit_category.html",{'cat':cat,'pro':pro})

def category_save(request,edit_id):
    if request.method=="POST":
        a = request.POST.get('category')
        b = request.POST.get('name')
        d = request.POST.get('price')
        try:
            image1 = request.FILES['image1']
            fs = FileSystemStorage()
            file1 = fs.save(image1.name,image1)
        except MultiValueDictKeyError:
            file1 = product_db.objects.get(id=edit_id).image1
        try:
            image2 = request.FILES['image2']
            fs = FileSystemStorage()
            file2 = fs.save(image2.name, image2)
        except MultiValueDictKeyError:
            file2 = product_db.objects.get(id=edit_id).image2
        try:
            image3 = request.FILES['image3']
            fs = FileSystemStorage()
            file3 = fs.save(image3.name, image3)
        except MultiValueDictKeyError:
            file3 =product_db.objects.get(id=edit_id).image3
        product_db.objects.filter(id=edit_id).update(category=a,item=b,price=d,image1=file1,image2=file2,image3=file3)
        messages.success(request, "Category Edited successfully!")
        return redirect(display_category)

def del_category(request,edit_id):
    x=product_db.objects.filter(id=edit_id)
    x.delete()
    return redirect(display_category)

def login_page(request):
    return render(request,"login1.html")
def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        ps = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=ps)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=ps
                # messages.success(request,"Welcome Admin")
                return redirect(home_page)
            else:
                messages.error(request, "Incorrect Username or Password")
                return redirect(login_page)
        else:
            messages.error(request, "User Not found")
            return redirect(login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)


