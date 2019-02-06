from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    # fields for meeting title, meeting date, meeting time,location, agenda
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    location=models.CharField(max_length=255)
    agenda=models.TextField()

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    # fields for meeting id (foreign key), attendance (many-to-many w/ User), minutes text
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingattendance=models.ManyToManyField(User)
    minutestext=models.TextField()
    
    def __str__(self):
        return self.minutestext
    
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    # fields for resource name, resource type, URL, date entered, user ID (foreign key w/ User), description
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'

class Event(models.Model):
    # fields for event title, location, date, time, description, user ID of member who posted it
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'

    
