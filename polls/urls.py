from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:pk>', views.MyNewView.as_view(), name='new_contact')
]