from django.forms import forms,ModelForm
from django import forms

from .models import Author,CreateBook

class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields='__all__'

class BookCreateForm(ModelForm):
    class Meta:
        model=CreateBook
        fields='__all__'

class OrderBookfrom(forms.Form):
    customer_name=forms.CharField()
    book_name=forms.ModelChoiceField(CreateBook.objects,required=False)
    no_of_copy=forms.IntegerField()
