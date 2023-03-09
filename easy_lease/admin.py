from django.contrib import admin

from .models import Property, Payment, Lease, Tenant

admin.site.register(Tenant)
admin.site.register(Property)
admin.site.register(Lease)
admin.site.register(Payment)
