# Пример моделей
class Author(models.Model):
name = models.CharField(max_length=100)

class Book(models.Model):
title = models.CharField(max_length=100)
authors = models.ManyToManyField(Author)

# Пример использования prefetch_related
books = Book.objects.prefetch_related('authors').all()
