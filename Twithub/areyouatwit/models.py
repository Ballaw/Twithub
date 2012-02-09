from django.db import models

# Create your models here.
class TwitOrNot(models.Model):
    twit = models.BooleanField()
    
    def __unicode__(self):
        return unicode(self.twit)

