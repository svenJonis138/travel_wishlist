from django.db import models


class Place(models.Model):
    """ Creates a model for the place object to be stored in DB """
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} visited? {self.visited}'
