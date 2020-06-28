from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    pro=Product.objects.all()
    context = {
        'proj_list':pro,
    }
    return render(request,'base.html',context)