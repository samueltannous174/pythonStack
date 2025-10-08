from django.db import models

class Books(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} {self.desc}"


class Authors(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    notes=models.CharField(max_length=45,default="sho ma badek")
    updated_at = models.DateTimeField(auto_now=True)
    books=models.ManyToManyField(Books,related_name="authors")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


def get_all_books():
    return Books.objects.all
def add_book(title,desc):
    return Books.objects.create(title=title,desc=desc)
def get_book(book_id):
    return Books.objects.get(id=book_id)
def get_book_authors(book_id):
    book = get_book(book_id)
    return book.authors
def add_author_to_book(author_id,book_id):
    book = get_book(book_id)
    author = get_author(author_id)
    book.authors.add(author)



def get_all_authors():
    return Authors.objects.all
def get_author(author_id):
    return Authors.objects.get(id=author_id)
def get_author_books(author_id):
    author = get_author(author_id)
    return author.books
def add_author(first_name,last_name):
    return Authors.objects.create(first_name=first_name,last_name=last_name)
