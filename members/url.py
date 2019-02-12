from django.conf.urls import url ,include
from django.urls import path
from members import view


urlpatterns = [
     url(r'^$', view.loginregisterpage, name='login_member'),
     path('register/',view.register,name='register'),
     path('login/',view.loginuser,name='login'),
     path('profile/',view.profile,name='profile'),
     path('logout/',view.logoutuser,name="logout"),
     path('roombooking/', view.roombook, name='roombook'),
     path('roombooking/formsubmit/', view.submit, name='submit'),
     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/$',
        view.activate, name='activate'),
     url(r'^activatedirector/(?P<uidb64>[0-9A-Za-z_\-]+)/$',
           view.director_activate, name='activatedirector'),

    # path('register/',views.register,name='register'),

]
