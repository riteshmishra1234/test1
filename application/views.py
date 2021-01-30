from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PurchaseOrderItem, PurchaseOrder
# Create your views here.


@login_required
def home(request):
    return render(request, 'application/home.html')

@login_required
def stock_incentive(request):
    return render(request, 'application/stock_incentive.html')

@login_required
def preorder_approval(request):
    return render(request, 'application/preorder_approval.html')
