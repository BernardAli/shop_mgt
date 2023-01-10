from django.contrib import admin
from .models import Category, Stock, Cash, CashHistory

# Register your models here.


admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(Cash)
admin.site.register(CashHistory)