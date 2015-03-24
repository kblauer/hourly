from django.contrib.auth.models import User
from django.db import models
from schedule.models import Schedule

# Creates a model for the ScheduleEntry item.  It essentially
# creates the schema in the database for the ScheduleEntry item,
# including all fields and types.  This represents the ScheduleEntry as
# a single item in a schedule.  Therefore each has a relationsip to both
# a user and a schedule.
class ScheduleEntry(models.Model):
    # The user that created the schedule event
    user = models.ForeignKey(User)
    schedule = models.ForeignKey(Schedule)
    title = models.CharField(max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()
    allDay = models.BooleanField()

    def __str__(self):
        return self.title