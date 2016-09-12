from django.db import models

# Create your models here.

class Customer(models.Model):
    """ Customer model """

    first_name = models.CharField(max_length=200, blank=True, null=True)
    fbid = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    machine_id = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    last_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.machine_id

class Ticket(models.Model):
    """ Ticket model """

    status = models.CharField(max_length=50, null=True, blank=True)
    fbid = models.CharField(max_length=200, blank=True, null=True)
    machine_id = models.CharField(max_length=200)
    message_text = models.TextField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    last_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.machine_id

