from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
def explorepage(request):
    users = User.objects.all()
    args={'users':users}
    return render(request,'explore.html',args)