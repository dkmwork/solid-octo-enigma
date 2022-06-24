from django.db import models

class Student(models.Model):
    s_id=models.IntegerField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    def __str__(self):
        return self.name

# Create your models here.
