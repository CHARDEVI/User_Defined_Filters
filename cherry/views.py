from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def usd_filters(request):
    d={'data':'Mahendra Singh Dhoni, commonly known as MS Dhoni'}
    return render(request,'usd_filters.html',d)