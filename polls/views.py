from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (DetailView,
                                  ListView,
                                  UpdateView,
                                  DeleteView,
                                  FormView)
from .models import Contact
from .forms import ContactForm, AddressForm
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ContactDetails(DetailView):
    model = Contact
    template_name = 'contact_details.html'
    context_object_name = 'user_contact'


class ContactView(FormView):
    template_name = 'register.html'
    form_class = ContactForm


class TestView(FormView):
    template_name = 'test.html'
    form_class = AddressForm
