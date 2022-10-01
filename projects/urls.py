
from django.urls import path
from . import views


#from .views import SignUpView



urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('project/', views.project, name="project"),
    path("signup/", views.signup, name="signup"),
    path('login/', views.loginUser, name="login"),
    path('main/', views.mainPage, name="main"),
    path('logout/', views.logoutUser, name="logout"),
    path('a_moneda/', views.a_moneda, name="a_moneda"),

]