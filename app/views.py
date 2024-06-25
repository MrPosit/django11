from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def list(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})

def detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'detail.html', {'book': book})

def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BookForm()
    return render(request, 'form.html', {'form': form})

def update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BookForm(instance=book)
    return render(request, 'form.html', {'form': form})

def delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list')
    return render(request, 'delete.html', {'book': book})
