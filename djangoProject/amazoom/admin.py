from django.contrib import admin

# Register your models here.
from amazoom.models import *

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Listing)