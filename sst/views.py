
from django.shortcuts import render, redirect
from .models import TestDetails, TestPaper
from django.contrib import messages


# from django.contrib.auth.models import user
# from django.contrib.auth import authenticate

def test_details(request):
    username = None
    if request.user.get_username():
        username = request.user.username
        test_details = TestDetails.objects.filter(user_id=username).order_by('-id')
        
        
        return render(request, 'sst/sst_details.html', {"test_details": test_details})
    
    else:
        messages.info('No DATA Found')
        return redirect(request, 'home')

        