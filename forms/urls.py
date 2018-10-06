from django.conf.urls import url ,include 
from django.urls import path 
from forms import views

urlpatterns = [
     url(r'^$', views.form_view, name='form_view'),
     path('formsubmit/',views.form_submit,name='form_submit'),
     

     ]