from django.shortcuts import render
from django.http import HttpResponse
from p_library.models import Book, Publishing_house
from django.template import loader
from django.shortcuts import redirect

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