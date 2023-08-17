from django.urls import path
from . import views
urlpatterns = [
    path('',views.explorepage,name="explorePage"),
]