from django.db import models
from django.contrib.auth.models import User

# Clienti
class Customer(models.Model):
  cardcode = models.CharField(max_length=12)
  customer = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  phone1 = models.CharField(max_length=12)
  phone2 = models.CharField(max_length=12)
  description = models.TextField(max_length=360)

  def __str__(self):
    return self.customer

# Lavori
class Work(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  work_date = models.DateField(auto_now=False, auto_now_add=False)
  description = models.TextField(max_length=255, blank=True)

  # Allegati
  attachment1 = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
  attachment2 = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
  attachment3 = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
  attachment4 = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
  attachment5 = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

  is_published = models.BooleanField(default=False)

  def __str__(self):
    return self.description