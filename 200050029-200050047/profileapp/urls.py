from django.urls import path
from . import views
urlpatterns = [
    path('',views.viewprofile,name="profilePage"),
    path('?P<pk>\d+',views.viewprofile,name="otherprofile"),
    path('update',views.profilepage,name="updateprofile")
]