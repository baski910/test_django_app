from django.db import models

# Create your models here.
class Book(models.Model):
    bookid = models.CharField(max_length=20)
    booktitle = models.CharField(max_length=50)
    bookauthor = models.CharField(max_length=50)
    class Meta:
        db_table = 'books'
