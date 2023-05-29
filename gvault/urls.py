from django.urls import path
from . import views
urlpatterns =[
    path("",views.index,name="index"),
    path("delete",views.delete,name="del"),
    path("abtus",views.abtus,name="abtus"),
    path("register",views.rreg,name="rreg"),
    path("abstract",views.abstract,name="abt"),
    path("login",views.loginuser,name="login"),
    path("profile",views.profile,name="profile"),
    path("logout",views.logoutuser,name="logout"),
    path("editprofile",views.edit,name="edit"),
    path("investor",views.investor,name="investor"),
    path("contact",views.contact,name="con"),
    path("tnc",views.tnc,name="tnc"),
    path("repository",views.repository,name="repository"),
]