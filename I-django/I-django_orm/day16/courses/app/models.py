from django.db import models

# Create your models here.

class Manager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 5:
            errors["name"] = "Name should be at least 5 characters"
        if len(post_data['desc']) < 15:
            errors["desc"] = "Description should be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()

    def __str__(self):
        return self.name


def add_course(Data):
    course = Course.objects.create(name=Data['title'], desc=Data['desc'])
    return course
def delete_course(id):
    course = Course.objects.get(id=id)
    course.delete()
def all_courses():
    courses = Course.objects.all()
    return courses

