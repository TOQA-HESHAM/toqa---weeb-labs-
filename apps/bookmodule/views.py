from django.shortcuts import render
from django.http import HttpResponse   
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Address, Student
from django.db.models import Count
from .models import Department
from .models import Course
from django.db.models import Min
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book





# new *
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

# new *
def index2(request, val1=0):
    return render(request, "bookmodule/index2.html", {"value1": val1})  


def viewbook(request, bookId): 
  # assume that we have the following books somewhere (e.g. database) 
  book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'} 
  book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'} 
  targetBook = None 
  if book1['id'] == bookId: targetBook = book1 
  if book2['id'] == bookId: targetBook = book2 
  context = {'book':targetBook} # book is the variable name accessible by the template 
  return render(request, 'bookmodule/show.html', context)


def index(request): 
  return render(request, "bookmodule/index.html") 
def list_books(request): 
  return render(request, 'bookmodule/list_books.html') 
def viewbook(request, bookId): 
  return render(request, 'bookmodule/one_book.html') 
def aboutus(request): 
  return render(request, 'bookmodule/aboutus.html') 

## lab5
def lab5(request):
    return render(request, "bookmodule/lab5.html")

## lab6
def search(request):
    return render(request, "bookmodule/search.html")

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/list_books.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')
## lab 7
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/list_books.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
                          .filter(title__icontains='and')\
                          .filter(edition__gte=2)\
                          .exclude(price__lte=100)[:10]

    if mybooks:
        return render(request, 'bookmodule/list_books.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
## lab 8

def task1_view(request):
    books = Book.objects.filter(Q(price__lte=80))  
    context = {'books': books}
    return render(request, 'bookmodule/list_books.html', context)


def task2_view(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    context = {'books': books}
    return render(request, 'bookmodule/list_books.html', context)



def task3_view(request):
    books = Book.objects.filter(
        ~(
            Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
        )
    )
    context = {'books': books}
    return render(request, 'bookmodule/list_books.html', context)

def task4_view(request):
    books = Book.objects.all().order_by('title')
    context = {'books': books}
    return render(request, 'bookmodule/list_books.html', context)




def task5_view(request):
    aggregation = Book.objects.aggregate(
        count_books=Count('id'),
        sum_prices=Sum('price'),
        avg_prices=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    context = {'aggregation': aggregation}
    return render(request, 'bookmodule/aggregation_result.html', context)



def task5_view(request):
    aggregation = Book.objects.aggregate(
        count_books=Count('id'),
        sum_prices=Sum('price'),
        avg_prices=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    context = {'aggregation': aggregation}
    return render(request, 'bookmodule/aggregation_result.html', context)



def task7_view(request):
    data = Address.objects.annotate(student_count=Count('student'))
    context = {'cities': data}
    return render(request, 'bookmodule/task7.html', context)

## lab 9
def lab9_task1(request):
    departments = Department.objects.annotate(num_students=Count('student'))
    return render(request, 'bookmodule/lab9_task1.html', {'departments': departments})    


def lab9_task2(request):
    courses = Course.objects.annotate(num_students=Count('student'))
    return render(request, 'bookmodule/lab9_task2.html', {'courses': courses}) 


def lab9_task3(request):
    departments = Department.objects.all()
    results = []
    for d in departments:
        oldest = d.student_set.order_by('id').first()
        if oldest:
            results.append({'department': d.name, 'student': oldest.name, 'id': oldest.id})
    return render(request, 'bookmodule/lab9_task3.html', {'results': results})   

def lab9_task4(request):
    departments = Department.objects.annotate(num_students=Count('student')).filter(num_students__gt=2).order_by('-num_students')
    return render(request, 'bookmodule/lab9_task4.html', {'departments': departments})        


## lab 10
def list_books_part1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/part1/list_books_part1.html', {'books': books})

def add_book_part1(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('lab9_part1_list')
    return render(request, 'bookmodule/part1/add_book.html')

def edit_book_part1(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('lab9_part1_list')
    return render(request, 'bookmodule/part1/edit_book.html', {'book': book})

def delete_book_part1(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('lab9_part1_list')        