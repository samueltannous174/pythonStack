from django.db import models

class Books(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Authors(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    notes=models.CharField(max_length=45,default="sho ma badek")
    updated_at = models.DateTimeField(auto_now=True)
    books=models.ManyToManyField(Books,related_name="authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"