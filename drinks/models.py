from django.db import models 


# inherit from models.Model so that django knows this is a model class

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name + ' ~ ' + self.description