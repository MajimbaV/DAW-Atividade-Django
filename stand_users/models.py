from django.db import models

# Create your models here.

class StandUser(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Stand(models.Model):
    name = models.CharField(max_length=100)
    ability = models.CharField(max_length=255)
    user = models.ForeignKey(StandUser, on_delete=models.CASCADE, related_name="+")
    
    def __str__(self) -> str:
        return self.name