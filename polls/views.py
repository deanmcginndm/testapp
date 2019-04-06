from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (DetailView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from .models import Contact
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class MyNewView(DetailView):
    model = Contact
    template_name = 'contact_details.html'
    context_object_name = 'user_contact'
