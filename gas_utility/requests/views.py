# Create your views here.

from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'request_form.html', {'form': form})

def request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'request_list.html', {'requests': requests})

def request_detail(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'request_detail.html', {'request': service_request})