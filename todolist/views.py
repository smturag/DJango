from django.shortcuts import redirect, render
from .models import user_info
from .forms import user_form

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
