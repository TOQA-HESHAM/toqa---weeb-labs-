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
]