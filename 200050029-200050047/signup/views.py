from django.shortcuts import render,redirect,HttpResponse
from signup.forms import RegForm
# Create your views here.
def signUp(request):
    if request.method=="POST":
        form=RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profileapp/update')
        else:
            return HttpResponse('Data Invalid')
    else:
            form=RegForm()

            args={'signupform':form}
            return render(request,'signup.html',args)