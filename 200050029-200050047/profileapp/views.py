from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from django.contrib.auth.models import User
from profileapp.models import Repository,Profile

import requests
import datetime

# Create your views here.
def viewprofile(request,pk=None):
        if pk:
            user=User.objects.get(pk=pk)
        else:
            user = get_object_or_404(User, id= request.user.id)
        
        profile=Profile.objects.filter(user=user).first()
        if profile!=None:
            repos=list(Repository.objects.filter(profile=profile))
            if repos==None:
                repos=[]
            args={'user':user,'profile':profile,'repos':repos}
            if pk:
                return render(request,'viewprofile.html',args)
            else:
                return render(request,'profileapp.html',args)

        else:
            return HttpResponse('Profile Not Available')


def profilepage(request,pk=None):
        if pk:
            user=User.objects.get(pk=pk)
        else:
            user = get_object_or_404(User, id= request.user.id)

        main_api='https://api.github.com/users/'

        url_followers=main_api+format(str(user.username))
        response_f=requests.get(url_followers)
        
        url_repos=main_api+format(str(user.username))+format(str('/repos'))
        response_r=requests.get(url_repos)

        if (response_f.status_code!=200) or (response_r.status_code!=200):
            return HttpResponse('Not Available')
    
        else:
            json_data_r=response_r.json()
            json_data_f=response_f.json()

            profile=Profile.objects.filter(user=user).first()
            if profile!=None:
                profile.followers=json_data_f["followers"]
                profile.save()

                repos=list(Repository.objects.filter(profile=profile))
                if repos!=None:
                    r=len(repos)
                    j=len(json_data_r)
                    
                    for i in range(0,j):
                        if(i>=r):
                            break
                        else:
                            repos[i].reponame=json_data_r[i]['name']
                            repos[i].stars=json_data_r[i]['stargazers_count']
                            repos[i].save()
                    if(j>=r):
                        for i in range(r,j):
                            repo=Repository(profile=profile,reponame=json_data_r[i]['name'],stars=json_data_r[i]['stargazers_count'])
                            repo.save()
                            repos.append(repo)
                else:
                    repos=[]



                    

                args={'user':user,'profile':profile,'repos':repos}
                redirect('/profileapp')
                return render(request,'profileapp.html',args)
            else:
                redirect('/profileapp')
                return HttpResponse('Profile Not Available')