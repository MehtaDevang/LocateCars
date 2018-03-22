from django.db import models

# Create your models here.

VEHICLE_STATUS = (
    ('runnning', 'running'),
    ('stopped', 'stopped'),
    ('scheduled', 'scheduled'),
)
class Vehicle(models.Model):
    name = models.CharField(max_length=30, null=False)
    dob = models.DateField(null=False)
    contact = models.CharField(max_length=10, null=False)
    vehicle_number = models.CharField(primary_key=True, max_length=6, null=False)
    vehicle_status = models.CharField(max_length=20, choices=VEHICLE_STATUS)

class Journey(models.Model):
    vehicle_id = models.ForeignKey('Vehicle')
    distance_covered = models.IntegerField()
    start_time = models.DateTimeField(auto_now_add=True, blank=False)
    last_update = models.DateTimeField();
    last_stoppage = models.CharField(max_length=100)
