from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def user_defined_validators(request):
    NFO=NameForm()
    d={'form':NFO}

    if request.method=='POST':
        FD=NameForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'user_defined_validators.html',d)