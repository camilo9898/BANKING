from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class Department(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class City(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10, blank=True, null=True)
    status = models.BooleanField(default=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} {self.abrev} {self.status}"

'''
User.add_to_class(
    'city',
    models.ForeignKey("City", on_delete=models.CASCADE, related_name="users", null=True, blank=True)
)

City.add_to_class(
    'department',
    models.ForeignKey("Department", on_delete=models.CASCADE, related_name="cities", null=True, blank=True)
)

Department.add_to_class(
    'country',
    models.ForeignKey("Country", on_delete=models.CASCADE, related_name="departments", null=True, blank=True)
)
'''