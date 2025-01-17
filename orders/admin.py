from django.contrib import admin
from . import models
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    raw_id_fields = ['product']



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','updated','paid']
    list_filter = ['paid']
    inlines = [OrderItemInline]