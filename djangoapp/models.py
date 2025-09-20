from django.db import models

class Student(models.Model):
    idStudent=models.IntegerField(primary_key=True)
    name=models.CharField()

class Account(models.Model):
    id=models.IntegerField()
    password=models.IntegerField()
    email=models.EmailField()
    student=models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)


class Owner(models.Model):
    name=models.CharField()

class Car(models.Model):
    brand=models.CharField()
    color=models.CharField()
    speed=models.CharField()
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)


class Author(models.Model):
    name=models.CharField()

class Book(models.Model):
    name=models.CharField()
    published_year=models.IntegerField()
    author=models.ManyToManyField(Author,through='Borrow')

class Borrow(models.Model):
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date=models.DateField()
    return_date=models.DateField()
