from django.urls import path
from adminapp import views

urlpatterns = [
    path('home_page/',views.home_page,name="home_page"),
    path('add_doctor/',views.add_doctor,name="add_doctor"),
    path('save_doctor/',views.save_doctor,name="save_doctor"),
    path('display_doctor/',views.display_doctor,name="display_doctor"),
    path('edit_doctor/<int:doc_id>/',views.edit_doctor,name="edit_doctor"),
    path('edit_save/<int:doc_id>/',views.edit_save,name="edit_save"),
    path('delete_doctor/<int:doc_id>/',views.delete_doctor,name="delete_doctor"),
    path('add_food/',views.add_food,name="add_food"),
    path('add_save/',views.add_save,name="add_save"),
    path('display_cat/',views.display_cat,name="display_cat"),
    path('edit_cat/<int:edit_id>/',views.edit_cat,name="edit_cat"),
    path('cat_save/<int:edit_id>/',views.cat_save,name="cat_save"),
    path('delete_category/<int:del_id>/',views.delete_category,name=" delete_category"),
    path('add_books/',views.add_books,name="add_books"),
    path('save_book/',views.save_book,name="save_book"),
    path('display_book/',views.display_book,name="display_book"),
    path('edit_book/<int:book_id>/',views.edit_book,name="edit_book"),
    path('book_edit/<int:book_id>/',views.book_edit,name="book_edit"),
    path('del_book/<int:book_id>',views.del_book,name="del_book"),
    path('category_page/',views.category_page,name="category_page"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:edit_id>/', views.edit_category,name="edit_category"),
    path('category_save/<int:edit_id>/', views.category_save,name="category_save"),
    path('del_category/<int:edit_id>/',views.del_category,name="del_category"),
    path('login_page/',views.login_page,name="login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout")


]