from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<slug:slug>', views.ContactDetails.as_view(), name='new_contact'),
    path('register/', views.ContactView.as_view(), name='registration_form'),
    path('test/', views.TestView.as_view(), name='test'),

]