from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from  .models import Book
from  .forms import BookForm

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to django</h1>")

def home(request):
    #msg = 'A mesage from view function'
    names = ['bob','tom','pat']
    return render(request,'simpleapp1/index.html',{'names': names})

def list_books(request):
    books = Book.objects.all()
    return render(request,'simpleapp1/books.html',{'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('simpleapp1:list_books'))
    else:
        form = BookForm()
        return render(request,'simpleapp1/addbooks.html',{'form': form})