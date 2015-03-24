from django.db import models
from django.contrib.auth.models import User

# Creates a model for the Schedule item.  It essentially
# creates the schema in the database for the Schedule item,
# including all fields and types.  This represents the schedule as a whole, 
# and does not contain any information regarding events within the schedule.
# a single schedule is currently simply an arbitrary grouping of calendar events 
# for the user's ease of organization.
class Schedule(models.Model):
    # The user that created the schedule
    user = models.ForeignKey(User)
    scheduleName = models.CharField(max_length=50)
    scheduleDescription = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.scheduleName