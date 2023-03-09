from django.contrib import admin

from .models import Property, Payment, Lease, Tenant


class TenantAdmin(admin.ModelAdmin):
    list_display = ('tenant_first_name',
                    'tenant_last_name',
                    'tenant_date_of_birth',
                    'tenant_profession',
                    'tenant_government_id',
                    'tenant_permanent_address',
                    'tenant_mobile_number',
                    'tenant_description'
                    )


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_name',
                    'property_owner',
                    'property_address',
                    'property_group_name',
                    'property_description'
                    )


class LeaseAdmin(admin.ModelAdmin):
    list_display = (
        'lease_tenant',
        'lease_property',
        'lease_advance',
        'lease_rent',
        'lease_start_date',
        'lease_due_date',
        'lease_state',
        'lease_state_node',
        'lease_description'
    )


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payment_date',
        'payment_amount',
        'payment_due_date',
        'payment_partial',
        'payment_paid'
    )


admin.site.register(Tenant, TenantAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Lease, LeaseAdmin)
admin.site.register(Payment, PaymentAdmin)
