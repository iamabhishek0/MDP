from django.conf.urls import url ,include
from django.urls import path
from members import view


urlpatterns = [
     url(r'^$', view.login_member, name='login_member'),
     path('register/',view.register,name='register'),
     path('login/',view.login_,name='login'),
    # path('register/',views.register,name='register'),

]
