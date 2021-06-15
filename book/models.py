from django.db import models

# Create your models here.

class Author(models.Model):
    author_name=models.CharField(max_length=100)
    choices=[
        ("Silver","Silver"),
        ("Gold", "Gold"),
        ("Platinum", "Platinum")
    ]
    royality=models.CharField(max_length=10,choices=choices)

    def __str__(self):
        return self.author_name

class CreateBook(models.Model):
    book_name=models.CharField(max_length=150)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    available_cpy=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.book_name

class OrderBook(models.Model):
    customer_name=models.CharField(max_length=100)
    book_name=models.ForeignKey(CreateBook,on_delete=models.CASCADE)
    no_of_copy=models.IntegerField()
    total=models.IntegerField()

    def __str__(self):
        return self.customer_name