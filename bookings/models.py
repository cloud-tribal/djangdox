from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    doc = models.FileField(upload_to="output")
    # address = models.CharField()
    # city =
    # arrival = models.DateField('Arrival')
    # departure = models.DateField('Departure')


    def __unicode__(self):
        return self.name
