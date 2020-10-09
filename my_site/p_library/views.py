from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from p_library.models import Book, Publishing_house, Author
from p_library.forms import AuthorForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Create your views here.
def ph_list(request):
    template = loader.get_template('home.html')
    phs = Publishing_house.objects.all()
    phs_data = {
        'publishing_houses': phs
    }
    return HttpResponse(template.render(phs_data))

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    lib_data = {
        'title': 'My library',
        'books': books
    }
    return HttpResponse(template.render(lib_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'