from django.db import models

# Create your models here.from django.db import models

class Profile(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField(max_length = 254)
  is_active = models.BooleanField(default=True)
  
  def __str__(self):
    return self.name
