from django.db import models

# Create your models here.
# for the tracks provided, we have 5 fields,
# but Django automatically adds the id field


class Track(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    duration = models.FloatField()
    last_play = models.DateTimeField()
