from django.db import models

# модель автора.
class Author(models.Model):  
    full_name = models.TextField()  # str
    birth_year = models.SmallIntegerField()  #int
    country = models.CharField(max_length=2)  # ограничение 2 симв

# модель книги
class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  #ограничение в 13 симв
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #поле внешнего ключа
    copy_count = models.SmallIntegerField(default=1, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=' ')
    redaction = models.ForeignKey('Publish', on_delete=models.CASCADE, null=True, blank=True, related_name='books')

# модель издательства
class Publish(models.Model):
       name = models.CharField(max_length=100)
def __str__(self):
    return self.name