from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Neighbourhood,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='Neighbor'
    return render(request,'NG/home.html',{'title':title})
@login_required(login_url='/accounts/login/')
def profile(request,id):
   user_object = request.user
   current_user = Profile.objects.get(username__id=request.user.id)
   user = Profile.objects.get(username__id=id)
   projects = Project.objects.all()
   return render(request, "NG/profile.html", {"current_user":current_user,"projects":projects,"user":user,"user_object":user_object})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
   current_user=request.user
   user_edit = Profile.objects.get(username__id=current_user.id)
   if request.method =='POST':
       form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
       if form.is_valid():
           form.save()
           return redirect('profile')
   else:
       form=ProfileForm(instance=request.user.profile)
   return render(request,'AW/edit_profile.html',locals())