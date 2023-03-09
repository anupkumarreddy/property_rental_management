from django.db import models


class Tenant(models.Model):
    tenant_first_name = models.CharField(max_length=50)
    tenant_last_name = models.CharField(max_length=50)
    tenant_date_of_birth = models.DateField()
    tenant_profession = models.CharField(max_length=50)
    tenant_government_id = models.CharField(max_length=50)
    tenant_permanent_address = models.CharField(max_length=500)
    tenant_mobile_number = models.CharField(max_length=12)
    tenant_description = models.CharField(max_length=500)

    def __str__(self):
        return self.tenant_first_name + " " + self.tenant_last_name


class Property(models.Model):
    property_name = models.CharField(max_length=50)
    property_owner = models.CharField(max_length=50)
    property_address = models.CharField(max_length=500)
    property_group_name = models.CharField(max_length=50)
    property_description = models.CharField(max_length=500)

    def __str__(self):
        return self.property_name


class Lease(models.Model):
    STATE_CHOICES = (
        ('EXPIRED', 'Lease expired'),
        ('ACTIVE', 'Lease running'),
        ('TERMINATED', 'lease terminated'),
    )
    lease_tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    lease_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    lease_advance = models.FloatField()
    lease_rent = models.FloatField()
    lease_start_date = models.DateField()
    lease_due_date = models.DateField()
    lease_state = models.CharField(max_length=10, choices=STATE_CHOICES)
    lease_state_node = models.CharField(max_length=100)
    lease_description = models.CharField(max_length=500)

    def __str__(self):
        return self.lease_tenant.tenant_first_name + self.lease_property.property_name


class Payment(models.Model):
    payment_lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.FloatField()
    payment_due_date = models.DateField()
    payment_partial = models.BooleanField()
    payment_paid = models.BooleanField()



