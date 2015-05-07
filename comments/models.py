from django.db import models
from django.contrib.auth.models import User
from schedule.models import Schedule


# Create your models here.
class ScheduleComment(models.Model):
    user = models.ForeignKey(User)
    schedule = models.ForeignKey(Schedule)
    comment = models.TextField()
    commentDate = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.comment