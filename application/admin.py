from django.contrib import admin
from .models import PurchaseOrder, PurchaseOrderItem, Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'status')
    list_filter = ('status',)
    search_fields = ['description','price', 'name']

class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('total', 'status','created_by','created_on','approved_by','approved_on')
    list_filter = ("status",)
    search_fields = ['approved_by', 'created_by']
    inlines = [PurchaseOrderItemInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
