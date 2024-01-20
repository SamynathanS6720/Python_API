from django.db import models

# Create your models here.
class Book( models.Model ):
    book_id = models.AutoField(primary_key=True)
    title = models.TextField()
    author = models.TextField()
    publisher = models.TextField()