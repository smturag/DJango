from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import user_info
from .forms import user_form
from django.http import HttpResponseRedirect

def user(request):
    userinfo = user_info.objects
    return render(request, 'index.html',{'userinfo': userinfo} )


def userform(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = user_form()
    return render(request, 'myform.html',{'form': form})

def findData(request):
    if request.method == 'POST':
        ids = request.POST.get('name')
        userinfo = user_info.objects.get(id = ids)
        print ( userinfo.name)
        return render(request, 'getdata.html',{'value': userinfo})
