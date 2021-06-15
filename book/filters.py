from .models import CreateBook
import django_filters

class BookFilter(django_filters.FilterSet):
    class Meta:
        model=CreateBook
        fields=['book_name','author']