from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import formset_factory

from p_library.models import Book, Publisher, Author, Friend
from p_library.forms import AuthorForm, BookForm, FriendForm


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorUpdate(UpdateView):
    model = Author
    success_url = reverse_lazy('p_library:author_list')
    fields = ['full_name', 'birth_year', 'country']
    template_name = 'author_edit.html'


class AuthorDelete(DeleteView):
    model = Author
    form_class = AuthorForm
    fields = ['full_name', 'birth_year', 'country']
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_delete.html'


class FriendCreate(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'


class FriendList(ListView):
    model = Friend
    template_name = 'friend_list.html'


class FriendUpdate(UpdateView):
    model = Friend
    success_url = reverse_lazy('p_library:friend_list')
    fields = ['full_name', 'birth_year']
    template_name = 'friend_edit.html'


class FriendDelete(DeleteView):
    model = Friend
    form_class = FriendForm
    fields = ['full_name', 'birth_year']
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_delete.html'


def publishers_list(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    publishers_data = {
        'publishers': publishers
    }
    return HttpResponse(template.render(publishers_data))


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
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            book.copy_count += 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='author')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='author')
    return render(request, 'manage_authors.html', {
        'author_formset': author_formset
    })


def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
        request,
        'manage_books_authors.html',
        {
            'author_formset': author_formset,
            'book_formset': book_formset
        }
    )