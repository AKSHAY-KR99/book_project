from django.shortcuts import render,redirect

from .models import Author,CreateBook,OrderBook
from .forms import AuthorForm,BookCreateForm,OrderBookfrom

from django.views.generic import TemplateView

from .filters import BookFilter

# Create your views here.
def mainpage(request):
    return render(request,'book/base.html')

class AuthorCreate(TemplateView):
    model=Author
    form_class=AuthorForm
    template_name = 'book/author.html'
    context={}
    def get(self, request, *args, **kwargs):
        books=self.model.objects.all()
        self.context['books']=books
        form=self.form_class
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("author")
        else:
            form = self.form_class(request.POST)
            self.context['form'] = form
            return render(request, self.template_name, self.context)

class AuthorDelete(TemplateView):
    model = Author
    template_name = 'book/author.html'
    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs['id'])
        book.delete()
        return redirect('author')

class AuthorEdit(TemplateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/author.html'
    context = {}
    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs['id'])
        form=self.form_class(instance=book)
        self.context['form'] = form
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        book = self.model.objects.get(id=kwargs['id'])
        form=self.form_class(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('author')
        else:
            book = self.model.objects.get(id=kwargs['id'])
            form = self.form_class(request.POST,instance=book)
            self.context['form'] = form
            return render(request, self.template_name, self.context)

class BookCreateView(TemplateView):
    model=CreateBook
    form_class=BookCreateForm
    template_name = 'book/createbook.html'
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookcreate')
        else:
            form = self.form_class(request.POST)
            self.context['form'] = form
            return render(request, self.template_name, self.context)

class ViewAllBooks(TemplateView):
    model=CreateBook
    template_name = 'book/all.html'
    context={}
    def get(self, request, *args, **kwargs):
        books=self.model.objects.all()
        self.context['books']=books
        return render(request,self.template_name,self.context)

class DeleteBook(TemplateView):
    model = CreateBook
    template_name = 'book/all.html'
    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs['id'])
        book.delete()
        return redirect('viewall')

class EditBook(TemplateView):
    model = CreateBook
    template_name = 'book/createbook.html'
    form_class=BookCreateForm
    context={}
    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs['id'])
        form=self.form_class(instance=book)
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        book = self.model.objects.get(id=kwargs['id'])
        form = self.form_class(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('viewall')
        else:
            book = self.model.objects.get(id=kwargs['id'])
            form = self.form_class(request.POST,instance=book)
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class BookOrder(TemplateView):
    model=OrderBook
    form_class= OrderBookfrom
    template_name = 'book/order.html'
    context={}
    def get(self, request, *args, **kwargs):
        book=CreateBook.objects.get(id=kwargs['id'])
        form=self.form_class(initial={'book_name':book})
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            customer_name=form.cleaned_data.get("customer_name")
            book_name=form.cleaned_data.get('book_name')
            no_of_copy=form.cleaned_data.get('no_of_copy')
            book=CreateBook.objects.get(book_name=book_name)




            if((book.available_cpy)>(no_of_copy)):
                total=(book.price)*no_of_copy
                bookings=self.model(customer_name=customer_name,book_name=book_name,no_of_copy=no_of_copy,total=total)
                bookings.save()
                return redirect("search")
            else:
                return render(request,'book/failed.html')





class SearchBook(TemplateView):
    model=CreateBook
    template_name = 'book/search.html'
    context={}
    def get(self, request, *args, **kwargs):
        books=CreateBook.objects.all()
        bookfilter=BookFilter(request.GET,queryset=books)
        self.context['filter']=bookfilter
        return render(request,self.template_name,self.context)

class ViewDetails(TemplateView):
    model=CreateBook
    template_name = 'book/details.html'
    context={}
    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs['id'])
        self.context['book']=book
        return render(request,self.template_name,self.context)