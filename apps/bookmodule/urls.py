from django.urls import path 
from . import views 
from .views import lab9_task1, lab9_task2, lab9_task3, lab9_task4
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
 ## lab 8
 path('task1/', views.task1_view, name='books.task1'),
 path('task2/', views.task2_view, name='books.task2'),
 path('task3/', views.task3_view, name='books.task3'),
 path('task4/', views.task4_view, name='books.task4'),
 path('task5/', views.task5_view, name='books.task5'),
 path('task7/', views.task7_view, name='books.task7'),
 ## lab 9
 path('lab9/task1/', lab9_task1, name='lab9_task1'),
 path('lab9/task2/', lab9_task2, name='lab9_task2'),
 path('lab9/task3/', lab9_task3, name='lab9_task3'),
 path('lab9/task4/', lab9_task4, name='lab9_task4'),
]