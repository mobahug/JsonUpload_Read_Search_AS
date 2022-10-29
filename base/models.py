from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class File(models.Model):
    file = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=["json"])]
    )

# similar database structure like in SQL when creating tables
# and specifying the column types
class Vehicle(models.Model):
    model_year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100, default="")
    rejection_percentage = models.CharField(max_length=10)
    reason_1 = models.CharField(max_length=100)
    reason_2 = models.CharField(max_length=100)
    reason_3 = models.CharField(max_length=100)
