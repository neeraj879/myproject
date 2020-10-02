from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import STUDENTS
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    now = datetime.datetime.now()
    return HttpResponse("<html><body>It is now %s.</body></html>" % now)

class CreateStudent(CreateView):
    model = STUDENTS
    fields = '__all__'
    template = 'student/SignUP.html'
    def form_valid(self, form):
        return super().form_valid(form)