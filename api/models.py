from django.db import models


class Investor(models.Model):
  full_name = models.CharField(max_length=200)
    
  def __str__(self):
    return self.title
