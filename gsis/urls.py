from django.urls import path
from . import views

urlpatterns = [
     path("",views.index,name='index'),

     # Authentication
     path('register-as-admin/', views.register_administrator, name='register-administrator'),
     path('register-as-staff/', views.register_staff, name='register-staff'),
     path('register-as-student/', views.register_student, name='register-student'),
     path("login/",views.login_view,name='login'),
     path('logout', views.logout_view, name='logout'),
     path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),

     #pages
     path("administrator/home",views.administrator,name='admin-home'),
     path("staff/home",views.staff,name='staff-home'),
     path("student/home",views.student,name='student-home'),
]