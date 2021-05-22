from django.shortcuts import render, redirect
from .models import *

def index(request):
    context={
        'all_books': Book.objects.all(),
    }
    return render(request, 'index.html', context)

def authors(request):
    context={
        'all_authors': Author.objects.all(),
    }
    return render(request, 'index.html', context)

def add_book(request):
    if request.method=="POST":
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def add_author(request):
    if request.method=="POST":
        Author.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], notes=request.POST['notes'])
    return redirect('/authors')

def view_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    the_authors = this_book.authors.all()
    remaining_authors = Author.objects.exclude(id__in=the_authors)
    context={
        'this_book': this_book,
        'the_authors': the_authors,
        'remaining_authors': remaining_authors,
    }
    return render(request, 'display.html', context)

def view_author(request, author_id):
    this_author = Author.objects.get(id=author_id)
    the_books = this_author.books.all()
    remaining_books = Book.objects.exclude(id__in=the_books)
    context={
        'this_author': this_author,
        'the_books': the_books,
        'remaining_books': remaining_books,
    }
    return render(request, 'display.html', context)

def add_auth_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    the_author = Author.objects.get(id=request.POST['author'])
    if request.method=="POST":
        the_author.books.add(this_book)
    return redirect(f'/book/{book_id}')

def add_book_auth(request, author_id):
    this_author = Author.objects.get(id=author_id)
    the_book = Book.objects.get(id=request.POST['book'])
    if request.method=="POST":
        the_book.authors.add(this_author)
    return redirect(f'/author/{author_id}')
