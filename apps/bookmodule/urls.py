from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>/', views.viewbook),

]

urlpatterns = [
 path('', views.index, name= "books.index"), 
 path('list_books/', views.list_books, name= "books.list_books"), 
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
 path('aboutus/', views.aboutus, name="books.aboutus"), 

 ## lab5
 path('lab5/', views.lab5, name='books.lab5'),
 ## lab6
 path('search', views.search_books, name='search_books'),
 #lab7
 path('simple/query', views.simple_query, name='simple_query'),
 path('complex/query', views.complex_query, name='complex_query'),
]