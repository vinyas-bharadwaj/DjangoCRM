from django.db import models

# Create your models here.
class Record(models.Model):
  
  # Stores the date and time when the record was created
  creation_date = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.CharField(max_length=20)
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  province = models.CharField(max_length=100)
  country = models.CharField(max_length=100)

  def __str__(self):
    return self.first_name + "   " + self.last_name
