from django.urls import path
from . import views

# 'simpleapp1:index'

urlpatterns = [
    #path('',views.index,name='index') # http://localhost:8000/app1/
    path('welcome',views.index,name='index'), # http://localhost:8000/app1/welcome
    path('home',views.home,name='home'),
    path('list_books',views.list_books,name='list_books'),
    path('create_book',views.create_book,name='create_book')
]