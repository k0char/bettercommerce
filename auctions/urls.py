from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/", views.create, name="create"),
    path("create/createrecord/", views.createrecord, name="createrecord"),
    path("categories/", views.categories, name='categories'),
    path("addcategory/", views.addcategory, name='addcategory'),
    path("addcategory/addcategoryrecord/", views.addcategory, name='addcategoryrecord')
]

urlpatterns += staticfiles_urlpatterns()