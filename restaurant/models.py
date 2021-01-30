from django.db import models

# Create your models here.
from django.db import models
from user_management.models import User

# Table occupancy status
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

food_status = (
    (0, "readymade"),
    (1, "To be prepared")
)

Order_STATUS = (
    (0, "Preparing"),
    (1, "Serve"),
    (2, "Served")
)


# tab_no is table number
class Table(models.Model):
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    mobile_no = models.CharField(max_length=10, unique=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="email")
    address = models.TextField(unique=True)
    tab_no = models.ForeignKey(Table, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_by")
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_by")

    def __str__(self):
        return self.id


class Waiter(models.Model):
    name = models.CharField(max_length=50, unique=True)
    mobile_no = models.CharField(max_length=10, unique=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="email")
    address = models.TextField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cashier(models.Model):
    fullname = models.CharField(max_length=50, unique=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="email")
    address = models.TextField(unique=True)
    mobile_no = models.CharField(max_length=10, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname


class Order_Item(models.Model):
    Cust_no = models.ForeignKey(Customer,on_delete=models.CASCADE())
    Item_name = models.CharField(max_length=50, unique=True)
    Item_price = models.DecimalField(max_digits=10, decimal_places=2)
    Item_quantity = models.IntegerField()
    food_status = models.IntegerField(choices=food_status, default=0)
    order_status = models.IntegerField(choices=Order_STATUS, default=2)

    def __str__(self):
        return self.Item_name

class Order_Bill(models.Model):
    Cust_no = models.ForeignKey(Customer, on_delete=models.CASCADE())
    total = models.DecimalField(max_length=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)


