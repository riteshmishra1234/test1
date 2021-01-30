from django.db import models
from user_management.models import User


#Pre Order Approval models
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

APPROVED_STATUS = ( 
    (0, "Unapproved"),
    (1, "Approved")
)

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    created_on =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

#po_no = purchase order no
class PurchaseOrder(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=APPROVED_STATUS, default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="approved_by")
    created_on =  models.DateTimeField(auto_now_add=True)
    approved_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class PurchaseOrderItem(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    po_no = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    created_on =  models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    
    
