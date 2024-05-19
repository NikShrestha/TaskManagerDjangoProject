
from django.contrib import admin
from django.urls import path
from ManagerApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # Route to the home view
    path('home/', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin')  # Route signin to the home view (index page)
]

