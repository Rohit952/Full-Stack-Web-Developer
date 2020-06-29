from django.db import models

# Create your models here.
class BasicInfo(models.Model):
    first_name = models.CharField(max_length=264,unique=True)
    last_name = models.CharField(max_length=264)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.first_name

class Marks(models.Model):
    name = models.ForeignKey(BasicInfo, on_delete = models.CASCADE)
    address = models.CharField(max_length=264,unique=True)
    english_marks = models.IntegerField()
    maths_marks = models.IntegerField()
    science_marks = models.IntegerField()

    def __str__(self):
        return str(self.name)
