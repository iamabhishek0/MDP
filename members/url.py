from django.conf.urls import url ,include
from django.urls import path
from members import view


urlpatterns = [
     url(r'^$', view.login, name='login'),
     path('register/',view.register,name='register'),
    # path('register/',views.register,name='register'),

]
