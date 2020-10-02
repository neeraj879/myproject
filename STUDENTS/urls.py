from django.urls import path
from .views import home, CreateStudent

urlpatterns = [
    path('',CreateStudent.as_view(),name="Signup"),
    path('home', home, name='student_home'),
]