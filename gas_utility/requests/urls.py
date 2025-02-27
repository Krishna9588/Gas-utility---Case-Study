from django.urls import path
from .views import submit_request, request_list, request_detail

urlpatterns = [
    path('submit/', submit_request, name='submit_request'),
    path('list/', request_list, name='request_list'),
    path('detail/<int:request_id>/', request_detail, name='request_detail'),
]