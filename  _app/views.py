from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def donation_list(request):
    return render(request, 'donations/donation_list.html')
